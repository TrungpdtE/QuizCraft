import random
import secrets
from dataclasses import dataclass, field
from typing import Any

from backend.services.data_service import DataService


FORM_KEYS = ("verb", "noun", "adjective", "adverb")


@dataclass
class ExerciseSession:
    session_id: str
    exercise_type: str
    filename: str
    mode: str
    questions: list[dict[str, Any]]
    order: list[int]
    position: int = 0
    phase: str = "main"
    resolved: bool = False
    answer_revealed: bool = False
    correct: int = 0
    incorrect: int = 0
    skipped: int = 0

    @property
    def current(self) -> dict[str, Any] | None:
        if self.position >= len(self.order):
            return None
        return self.questions[self.order[self.position]]

    @property
    def score(self) -> dict[str, int]:
        return {
            "correct": self.correct,
            "incorrect": self.incorrect,
            "skipped": self.skipped,
        }


class SessionService:
    def __init__(self, data_service: DataService) -> None:
        self.data_service = data_service
        self.sessions: dict[str, ExerciseSession] = {}

    def start(self, exercise_type: str, filename: str, mode: str) -> ExerciseSession:
        if mode not in {"sequential", "random"}:
            raise ValueError("Mode phải là sequential hoặc random")
        questions = self.data_service.load(exercise_type, filename)
        order = list(range(len(questions)))
        if mode == "random":
            random.SystemRandom().shuffle(order)
        session = ExerciseSession(
            session_id=secrets.token_urlsafe(16),
            exercise_type=exercise_type,
            filename=filename,
            mode=mode,
            questions=questions,
            order=order,
        )
        self.sessions[session.session_id] = session
        return session

    def get(self, session_id: str) -> ExerciseSession:
        session = self.sessions.get(session_id)
        if not session:
            raise KeyError("Session không tồn tại hoặc đã hết hạn")
        return session

    def public_question(self, session: ExerciseSession) -> dict[str, Any] | None:
        item = session.current
        if item is None:
            return None
        number = session.position + 1
        if session.exercise_type == "word_forms":
            question: dict[str, Any] = {
                "number": number,
                "prompt": "Từ này trong tiếng Anh là gì?",
                "vietnamese": item["vietnamese"],
                "phase": session.phase,
            }
            if session.phase == "forms":
                question["english"] = item["english"]
                question["form_fields"] = [
                    key for key in FORM_KEYS if item.get("forms", {}).get(key)
                ]
            return question
        if session.exercise_type == "word_types":
            return {
                "number": number,
                "sentence": item["sentence"],
                "tokens": [{"word": token["word"]} for token in item["tokens"]],
            }
        return {
            "number": number,
            "id": item.get("id"),
            "question": item["question"],
            "options": item["options"],
            "tags": item.get("tags", []),
        }

    def submit(self, session: ExerciseSession, answer: Any) -> dict[str, Any]:
        if not session.current:
            raise ValueError("Lượt làm bài đã hoàn thành")
        if session.resolved:
            raise ValueError("Câu này đã được xử lý, hãy chọn Next")
        if session.answer_revealed:
            raise ValueError("Đáp án đã được hiển thị, hãy chọn Next")
        if session.exercise_type == "word_forms":
            return self._submit_word_forms(session, answer)
        if session.exercise_type == "word_types":
            return self._submit_word_types(session, answer)
        return self._submit_multiple_choice(session, answer)

    def skip(self, session: ExerciseSession) -> None:
        if not session.current:
            raise ValueError("Lượt làm bài đã hoàn thành")
        if not session.resolved:
            session.skipped += 1
            session.resolved = True
        session.answer_revealed = True

    def reveal(self, session: ExerciseSession) -> Any:
        item = session.current
        if not item:
            raise ValueError("Lượt làm bài đã hoàn thành")
        session.answer_revealed = True
        if session.exercise_type == "word_forms":
            return {"english": item["english"], "forms": item.get("forms", {})}
        if session.exercise_type == "word_types":
            return [token["type"] for token in item["tokens"]]
        return {
            "option": item["answer"],
            "text": item["options"].get(item["answer"], ""),
        }

    def next_question(self, session: ExerciseSession) -> None:
        if not session.current:
            return
        if not session.resolved and not session.answer_revealed:
            raise ValueError("Hãy Submit, Skip hoặc Show Answer trước khi chuyển câu")
        session.position += 1
        session.phase = "main"
        session.resolved = False
        session.answer_revealed = False

    def _submit_word_forms(self, session: ExerciseSession, answer: Any) -> dict[str, Any]:
        item = session.current or {}
        if session.phase == "main":
            value = answer.get("english", "") if isinstance(answer, dict) else str(answer)
            correct = _normalize(value) == _normalize(item["english"])
            if correct:
                if not any(item.get("forms", {}).get(key) for key in FORM_KEYS):
                    session.correct += 1
                    session.resolved = True
                    return {
                        "correct": True,
                        "field_results": {"english": True},
                        "correct_answer": item["english"],
                        "phase": "main",
                    }
                session.phase = "forms"
                return {
                    "correct": True,
                    "field_results": {"english": True},
                    "correct_answer": item["english"],
                    "phase": "forms",
                    "question": self.public_question(session),
                }
            session.incorrect += 1
            session.resolved = True
            return {
                "correct": False,
                "field_results": {"english": False},
                "correct_answer": {"english": item["english"], "forms": item.get("forms", {})},
                "phase": "main",
            }

        submitted = answer if isinstance(answer, dict) else {}
        expected = item.get("forms", {})
        results = {
            key: _normalize(submitted.get(key, "")) == _normalize(expected[key])
            for key in FORM_KEYS
            if expected.get(key)
        }
        correct = all(results.values())
        session.correct += int(correct)
        session.incorrect += int(not correct)
        session.resolved = True
        return {
            "correct": correct,
            "field_results": results,
            "correct_answer": expected,
            "phase": "forms",
        }

    def _submit_word_types(self, session: ExerciseSession, answer: Any) -> dict[str, Any]:
        values = answer if isinstance(answer, list) else []
        expected = [token["type"].upper() for token in (session.current or {})["tokens"]]
        results = {
            str(index): index < len(values) and str(values[index]).strip().upper() == expected[index]
            for index in range(len(expected))
        }
        correct = all(results.values())
        session.correct += int(correct)
        session.incorrect += int(not correct)
        session.resolved = True
        return {
            "correct": correct,
            "field_results": results,
            "correct_answer": expected,
            "phase": "main",
        }

    def _submit_multiple_choice(self, session: ExerciseSession, answer: Any) -> dict[str, Any]:
        item = session.current or {}
        value = answer.get("option", "") if isinstance(answer, dict) else str(answer)
        correct = value.strip().upper() == item["answer"].upper()
        session.correct += int(correct)
        session.incorrect += int(not correct)
        session.resolved = True
        return {
            "correct": correct,
            "field_results": {value.strip().upper(): correct} if value else {},
            "correct_answer": {
                "option": item["answer"],
                "text": item["options"].get(item["answer"], ""),
            },
            "phase": "main",
        }


def _normalize(value: Any) -> str:
    return " ".join(str(value).strip().casefold().split())

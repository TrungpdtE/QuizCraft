import json
import re
from pathlib import Path
from typing import Any


class ExerciseParseError(ValueError):
    pass


def parse_json_objects(path: Path) -> list[dict[str, Any]]:
    text = _without_comment_lines(path.read_text(encoding="utf-8"))
    decoder = json.JSONDecoder()
    items: list[dict[str, Any]] = []
    position = 0

    while position < len(text):
        while position < len(text) and (text[position].isspace() or text[position] == ","):
            position += 1
        if position >= len(text):
            break
        try:
            value, position = decoder.raw_decode(text, position)
        except json.JSONDecodeError as exc:
            raise ExerciseParseError(f"{path.name}: JSON không hợp lệ tại dòng {exc.lineno}") from exc
        if isinstance(value, list):
            items.extend(value)
        elif isinstance(value, dict):
            items.append(value)
        else:
            raise ExerciseParseError(f"{path.name}: mỗi bài phải là một object JSON")

    if not items:
        raise ExerciseParseError(f"{path.name}: không tìm thấy dữ liệu")
    return items


def parse_multiple_choice(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if re.search(r"^###\s+Q\d+", text, flags=re.MULTILINE):
        questions = _parse_markdown_checkboxes(text)
    else:
        questions = _parse_numbered_questions(text)
    if not questions:
        raise ExerciseParseError(f"{path.name}: không tìm thấy câu hỏi trắc nghiệm")
    return questions


def _parse_markdown_checkboxes(text: str) -> list[dict[str, Any]]:
    answer_key: dict[str, str] = {
        match.group(1).upper(): match.group(2).upper()
        for match in re.finditer(
            r"^\s*-\s*(Q\d+)\s*:\s*([A-Z])\b",
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )
    }
    question_section = re.split(r"^##\s+Answer Key\s*$", text, maxsplit=1, flags=re.MULTILINE)[0]
    headers = list(
        re.finditer(
            r"^###\s+(Q\d+)([^\n]*)\n+",
            question_section,
            flags=re.MULTILINE | re.IGNORECASE,
        )
    )
    results: list[dict[str, Any]] = []

    for index, header in enumerate(headers):
        block_end = headers[index + 1].start() if index + 1 < len(headers) else len(question_section)
        block = question_section[header.end() : block_end].strip()
        option_matches = list(
            re.finditer(
                r"^\s*-\s*\[[ xX]?\]\s*([A-Z])\.\s*(.+?)\s*$",
                block,
                flags=re.MULTILINE,
            )
        )
        if not option_matches:
            continue
        question_text = block[: option_matches[0].start()].strip()
        question_id = header.group(1).upper()
        answer = answer_key.get(question_id)
        if not answer:
            inline = re.search(r"^Answer\s*:\s*([A-Z])\b", block, flags=re.MULTILINE | re.IGNORECASE)
            answer = inline.group(1).upper() if inline else None
        if not answer:
            continue
        tags = re.findall(r"\[([^\]]+)\]", header.group(2))
        results.append(
            {
                "id": question_id,
                "question": question_text,
                "options": {match.group(1).upper(): match.group(2).strip() for match in option_matches},
                "answer": answer,
                "tags": tags,
            }
        )
    return results


def _parse_numbered_questions(text: str) -> list[dict[str, Any]]:
    starts = list(re.finditer(r"^\s*(\d+)[.)]\s+(.+?)\s*$", text, flags=re.MULTILINE))
    results: list[dict[str, Any]] = []
    for index, start in enumerate(starts):
        block_end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[start.end() : block_end]
        options = {
            match.group(1).upper(): match.group(2).strip()
            for match in re.finditer(
                r"^\s*(?:[-*]\s*)?([A-Z])[.)]\s+(.+?)\s*$",
                block,
                flags=re.MULTILINE,
            )
        }
        answer_match = re.search(
            r"^\s*(?:Answer|Đáp án)\s*:\s*([A-Z])\b",
            block,
            flags=re.MULTILINE | re.IGNORECASE,
        )
        if options and answer_match:
            results.append(
                {
                    "id": str(start.group(1)),
                    "question": start.group(2).strip(),
                    "options": options,
                    "answer": answer_match.group(1).upper(),
                    "tags": [],
                }
            )
    return results


def _without_comment_lines(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#"))

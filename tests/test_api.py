from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_frontend_is_served() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "English Practice" in response.text


def start(exercise_type: str, filename: str, mode: str = "sequential") -> dict:
    response = client.get(
        "/api/exercises/start",
        params={"type": exercise_type, "file": filename, "mode": mode},
    )
    assert response.status_code == 200
    return response.json()


def test_types_and_files() -> None:
    types = client.get("/api/exercises/types")
    assert types.status_code == 200
    assert {item["id"] for item in types.json()} == {
        "word_forms",
        "word_types",
        "multiple_choice",
    }

    files = client.get("/api/exercises/files", params={"type": "multiple_choice"})
    assert files.status_code == 200
    assert "ai_engineering_1000.md" in files.json()["files"]


def test_word_form_two_phase_flow() -> None:
    data = start("word_forms", "basic.txt")
    session_id = data["session_id"]

    first = client.post(
        "/api/exercises/submit",
        json={"session_id": session_id, "answer": {"english": "produce"}},
    )
    assert first.status_code == 200
    assert first.json()["phase"] == "forms"

    second = client.post(
        "/api/exercises/submit",
        json={
            "session_id": session_id,
            "answer": {
                "verb": "produce",
                "noun": "production",
                "adjective": "productive",
                "adverb": "productively",
            },
        },
    )
    assert second.status_code == 200
    assert second.json()["correct"] is True
    assert second.json()["score"]["correct"] == 1


def test_random_session_has_unique_question_order() -> None:
    data = start("multiple_choice", "basic.txt", "random")
    session_id = data["session_id"]
    seen = []

    while True:
        question_response = client.get(
            "/api/exercises/question", params={"session_id": session_id}
        ).json()
        if question_response["completed"]:
            break
        seen.append(question_response["question"]["id"])
        client.post("/api/exercises/skip", json={"session_id": session_id})
        client.post("/api/exercises/next", json={"session_id": session_id})

    assert len(seen) == 3
    assert len(set(seen)) == 3


def test_path_traversal_is_rejected() -> None:
    response = client.get(
        "/api/exercises/start",
        params={
            "type": "multiple_choice",
            "file": "../../Multiple choice.md",
            "mode": "sequential",
        },
    )
    assert response.status_code == 400

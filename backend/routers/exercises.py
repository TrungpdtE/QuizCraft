from typing import Any

from fastapi import APIRouter, HTTPException, Query

from backend.models.schemas import SessionRequest, SubmitRequest
from backend.services.data_service import DataService
from backend.services.parsers import ExerciseParseError
from backend.services.session_service import ExerciseSession, SessionService


router = APIRouter(prefix="/api/exercises", tags=["exercises"])
data_service = DataService()
session_service = SessionService(data_service)


@router.get("/types")
def get_types() -> list[dict[str, str]]:
    return data_service.list_types()


@router.get("/files")
def get_files(type: str = Query(...)) -> dict[str, Any]:
    try:
        return {"type": type, "files": data_service.list_files(type)}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/start")
def start_exercise(
    type: str = Query(...),
    file: str = Query(...),
    mode: str = Query("sequential"),
) -> dict[str, Any]:
    try:
        session = session_service.start(type, file, mode)
        return _session_payload(session)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except (ValueError, ExerciseParseError, KeyError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/question")
def get_question(session_id: str = Query(...)) -> dict[str, Any]:
    session = _get_session(session_id)
    return _question_payload(session)


@router.post("/submit")
def submit_answer(payload: SubmitRequest) -> dict[str, Any]:
    session = _get_session(payload.session_id)
    try:
        result = session_service.submit(session, payload.answer)
        return {**result, "score": session.score}
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@router.post("/skip")
def skip_question(payload: SessionRequest) -> dict[str, Any]:
    session = _get_session(payload.session_id)
    try:
        session_service.skip(session)
        return {
            "message": "Đã bỏ qua câu hỏi",
            "answer": session_service.reveal(session),
            "score": session.score,
        }
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@router.get("/answer")
def show_answer(session_id: str = Query(...)) -> dict[str, Any]:
    session = _get_session(session_id)
    try:
        return {"answer": session_service.reveal(session), "score": session.score}
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@router.post("/next")
def next_question(payload: SessionRequest) -> dict[str, Any]:
    session = _get_session(payload.session_id)
    try:
        session_service.next_question(session)
        return _question_payload(session)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


def _get_session(session_id: str) -> ExerciseSession:
    try:
        return session_service.get(session_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


def _session_payload(session: ExerciseSession) -> dict[str, Any]:
    return {
        "session_id": session.session_id,
        "exercise_type": session.exercise_type,
        "mode": session.mode,
        "file": session.filename,
        "total": len(session.questions),
        "question": session_service.public_question(session),
        "score": session.score,
    }


def _question_payload(session: ExerciseSession) -> dict[str, Any]:
    return {
        "session_id": session.session_id,
        "question": session_service.public_question(session),
        "score": session.score,
        "progress": {
            "current": min(session.position + 1, len(session.questions)),
            "total": len(session.questions),
        },
        "completed": session.current is None,
    }

from typing import Any, Literal

from pydantic import BaseModel, Field


ExerciseType = Literal["word_forms", "word_types", "multiple_choice"]
ExerciseMode = Literal["sequential", "random"]


class SubmitRequest(BaseModel):
    session_id: str
    answer: Any


class SessionRequest(BaseModel):
    session_id: str


class StartResponse(BaseModel):
    session_id: str
    exercise_type: ExerciseType
    mode: ExerciseMode
    file: str
    total: int
    question: dict[str, Any] | None
    score: dict[str, int]


class QuestionResponse(BaseModel):
    session_id: str
    question: dict[str, Any] | None
    score: dict[str, int]
    progress: dict[str, int]
    completed: bool = False


class SubmitResponse(BaseModel):
    correct: bool
    field_results: dict[str, bool] = Field(default_factory=dict)
    correct_answer: Any = None
    question: dict[str, Any] | None = None
    score: dict[str, int]
    phase: str | None = None

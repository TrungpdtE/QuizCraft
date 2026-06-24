from pathlib import Path
from typing import Any

from backend.services.parsers import parse_json_objects, parse_multiple_choice


DATABASE_DIR = Path(__file__).resolve().parent.parent / "database"
EXERCISE_TYPES = {
    "word_forms": "Word Form",
    "word_types": "Word Type",
    "multiple_choice": "Multiple Choice",
}
ALLOWED_EXTENSIONS = {".txt", ".json", ".md"}


class DataService:
    def list_types(self) -> list[dict[str, str]]:
        return [{"id": key, "name": value} for key, value in EXERCISE_TYPES.items()]

    def list_files(self, exercise_type: str) -> list[str]:
        folder = self._type_folder(exercise_type)
        return sorted(
            path.name
            for path in folder.iterdir()
            if path.is_file() and path.suffix.lower() in ALLOWED_EXTENSIONS
        )

    def load(self, exercise_type: str, filename: str) -> list[dict[str, Any]]:
        path = self._safe_file(exercise_type, filename)
        if exercise_type == "multiple_choice":
            return parse_multiple_choice(path)
        return parse_json_objects(path)

    def _type_folder(self, exercise_type: str) -> Path:
        if exercise_type not in EXERCISE_TYPES:
            raise ValueError("Dạng bài không hợp lệ")
        folder = DATABASE_DIR / exercise_type
        folder.mkdir(parents=True, exist_ok=True)
        return folder

    def _safe_file(self, exercise_type: str, filename: str) -> Path:
        if not filename or Path(filename).name != filename:
            raise ValueError("Tên file không hợp lệ")
        path = (self._type_folder(exercise_type) / filename).resolve()
        if path.parent != self._type_folder(exercise_type).resolve() or not path.is_file():
            raise FileNotFoundError(f"Không tìm thấy file: {filename}")
        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            raise ValueError("Định dạng file không được hỗ trợ")
        return path

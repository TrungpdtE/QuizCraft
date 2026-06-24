from pathlib import Path

from backend.services.parsers import parse_json_objects, parse_multiple_choice


ROOT = Path(__file__).resolve().parents[1]
DATABASE = ROOT / "backend" / "database"


def test_parse_concatenated_json_objects() -> None:
    items = parse_json_objects(DATABASE / "word_forms" / "basic.txt")
    assert len(items) == 4
    assert items[0]["forms"]["noun"] == "production"


def test_parse_simple_multiple_choice() -> None:
    items = parse_multiple_choice(DATABASE / "multiple_choice" / "basic.txt")
    assert len(items) == 3
    assert items[0]["answer"] == "B"
    assert items[1]["options"]["C"] == "production"


def test_parse_markdown_multiple_choice_and_answer_key() -> None:
    items = parse_multiple_choice(
        DATABASE / "multiple_choice" / "ai_engineering_1000.md"
    )
    assert len(items) == 1000
    assert items[0]["id"] == "Q0001"
    assert items[0]["answer"] == "B"
    assert items[-1]["id"] == "Q1000"
    assert items[-1]["answer"] == "A"

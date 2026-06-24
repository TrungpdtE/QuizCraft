import re
from pathlib import Path

from backend.services.parsers import parse_json_objects


ROOT = Path(__file__).resolve().parents[1]
DATABASE = ROOT / "backend" / "database"
ALLOWED_WORD_TYPES = {"N", "V", "ADJ", "ADV", "AR", "P", "PRON", "CONJ", "DET"}


def test_all_generated_word_form_lessons_are_valid() -> None:
    files = sorted((DATABASE / "word_forms").glob("[0-9][0-9]_*.json"))
    assert len(files) == 6
    assert sum(len(parse_json_objects(path)) for path in files) == 180

    for path in files:
        for item in parse_json_objects(path):
            assert item["vietnamese"].strip()
            assert item["english"].strip()
            assert item["forms"]
            assert set(item["forms"]) <= {"verb", "noun", "adjective", "adverb"}
            assert all(value.strip() for value in item["forms"].values())


def test_all_generated_word_type_lessons_are_valid() -> None:
    files = sorted((DATABASE / "word_types").glob("[0-9][0-9]_*.json"))
    assert len(files) == 6
    assert sum(len(parse_json_objects(path)) for path in files) == 120

    for path in files:
        for item in parse_json_objects(path):
            assert item["sentence"].strip()
            assert len(item["tokens"]) >= 5
            assert all(token["type"] in ALLOWED_WORD_TYPES for token in item["tokens"])

            sentence_words = re.findall(r"[A-Za-z]+", item["sentence"])
            token_words = [token["word"] for token in item["tokens"]]
            assert sentence_words == token_words

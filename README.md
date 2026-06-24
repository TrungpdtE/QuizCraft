# English Learning App

Ứng dụng fullstack luyện tiếng Anh với FastAPI và HTML/CSS/JavaScript thuần.

## Tính năng

- Ba dạng bài: Word Form, Word Type, Multiple Choice.
- Chọn file dữ liệu riêng cho từng bài.
- Chế độ `sequential` và `random`.
- Random xáo trộn toàn bộ câu một lần nên không lặp câu trong cùng session.
- Submit, Skip, Show Answer, Next và thống kê đúng/sai/bỏ qua.
- Parser Multiple Choice hỗ trợ:
  - Format `1. Question`, `A. option`, `Answer: A`.
  - Markdown checkbox `### Q0001`, `- [ ] A. option` và Answer Key cuối file.
- File `Multiple choice.md` ban đầu đã được đưa vào
  `backend/database/multiple_choice/ai_engineering_1000.md` với đủ 1.000 câu.

## Cấu trúc

```text
backend/
├── main.py
├── routers/exercises.py
├── services/
│   ├── data_service.py
│   ├── parsers.py
│   └── session_service.py
├── models/schemas.py
└── database/
    ├── word_forms/
    ├── word_types/
    └── multiple_choice/
frontend/
├── index.html
├── style.css
└── app.js
tests/
```

## Chạy ứng dụng

Yêu cầu Python 3.10 trở lên.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m uvicorn backend.main:app --reload
```

Mở <http://127.0.0.1:8000>. API docs ở
<http://127.0.0.1:8000/docs>.

## Chạy test

```bash
python3 -m pytest
```

## Thêm dữ liệu

### Word Form và Word Type

Thêm file `.txt` hoặc `.json` vào folder tương ứng. File có thể chứa:

- Nhiều JSON object nối tiếp nhau, cách nhau bằng dòng trống.
- Hoặc một JSON array chứa các object.

Các dòng bắt đầu bằng `#` được xem là chú thích.

### Multiple Choice

Thêm `.txt` hoặc `.md` vào `backend/database/multiple_choice/`. Ví dụ:

```text
1. What does "reduce" mean?
A. tăng
B. giảm
C. sửa
D. xoá
Answer: B
```

## API

- `GET /api/exercises/types`
- `GET /api/exercises/files?type=word_forms`
- `GET /api/exercises/start?type=word_forms&file=basic.txt&mode=random`
- `GET /api/exercises/question?session_id=...`
- `POST /api/exercises/submit`
- `POST /api/exercises/skip`
- `GET /api/exercises/answer?session_id=...`
- `POST /api/exercises/next`

Các API sau khi start dùng `session_id` trả về từ `/start`.

Ví dụ submit:

```json
{
  "session_id": "SESSION_ID",
  "answer": {"option": "B"}
}
```

Session hiện được lưu trong RAM. Khi restart server, các session đang làm sẽ mất;
điều này phù hợp cho bản chạy local/MVP.

## Bộ bài học cấp tốc

Project có thêm bộ dữ liệu học theo lộ trình:

### Word Forms — 180 họ từ

1. `01_daily_communication.json`: giao tiếp hằng ngày.
2. `02_workplace_english.json`: công việc và làm việc nhóm.
3. `03_intern_interview.json`: ứng tuyển và phỏng vấn intern.
4. `04_backend_engineering.json`: lập trình và vận hành backend.
5. `05_api_database_systems.json`: API, database và distributed systems.
6. `06_ai_engineering.json`: AI/ML, RAG, LLM và agent.

### Word Types — 120 câu

1. `01_grammar_foundation.json`: nền tảng nhận diện loại từ.
2. `02_daily_communication.json`: câu giao tiếp thường gặp.
3. `03_workplace_interview.json`: công sở và phỏng vấn.
4. `04_backend_api_database.json`: backend, API và database.
5. `05_system_design_security.json`: system design và security.
6. `06_ai_ml_llm.json`: machine learning, LLM và production AI.

Nên học theo đúng thứ tự file. Với mỗi file, làm `sequential` lần đầu để học,
sau đó làm lại bằng `random` cho đến khi đạt ít nhất 90%.

Nếu cần dựng lại các file JSON từ nguồn dữ liệu đã biên soạn:

```bash
python3 scripts/build_lesson_data.py
```

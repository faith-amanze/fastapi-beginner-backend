# Beginner AI Assistant API

A beginner-friendly FastAPI backend with four endpoints. The chat, quiz, and summarise routes use placeholder logic; no AI model or API key is required.

## Project Structure

```text
fastapi_beginner_backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routers/
│       ├── __init__.py
│       ├── health.py
│       ├── chat.py
│       ├── quiz.py
│       └── summarise.py
├── docs/
│   └── api-test-report.md
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```

## Setup (Windows PowerShell)

Open PowerShell in the project root directory and run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the API

From the project root, run:

```powershell
uvicorn app.main:app --reload
```

Open Swagger UI in your browser:

http://127.0.0.1:8000/docs

The alternative API documentation is available at:

http://127.0.0.1:8000/redoc

## Endpoints

- `GET /health` — Returns the API status, version, and UTC timestamp. It does not call an AI model.
- `POST /chat` — Accepts a message and returns a structured answer.
- `POST /quiz` — Accepts a topic and the number of questions to generate (1–10).
- `POST /summarise` — Accepts text and the maximum number of summary bullets (1–10).

## Example Request Bodies

### Chat

```json
{
  "message": "What is Python?"
}
```

### Quiz

```json
{
  "topic": "Python",
  "number_of_questions": 3
}
```

### Summarise

```json
{
  "text": "FastAPI is a Python framework. It helps developers build APIs.",
  "max_bullets": 2
}
```

## Run Automated Tests

From the project root, run:

```powershell
python -m pytest
```

The automated tests cover:
- The health endpoint.
- A valid chat request.
- An invalid chat request.

All three automated tests passed successfully.

A detailed test record is available in `docs/api-test-report.md`.

## Notes

Pydantic validates the request bodies. Invalid values produce HTTP 422 validation responses automatically.

The current chat, quiz, and summarisation feature logic is intentionally simple and uses placeholder responses. Real AI functionality can be integrated later, after the API structure is working correctly.
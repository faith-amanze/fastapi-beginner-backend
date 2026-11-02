# API Test Report

## Environment
- Framework: FastAPI
- Validation: Pydantic
- Automated test tools: pytest and FastAPI TestClient (httpx)

## Endpoints Tested

| Endpoint | Test Input | Expected Result | Actual Result |
|---|---|---|---|
| `GET /health` | No body | HTTP 200 with status, version, and timestamp | Passed |
| `POST /chat` | `{"message":"Hello"}` | HTTP 200 with answer, source, and success fields | Passed |
| `POST /quiz` | `{"topic":"Python","number_of_questions":5}` | HTTP 200 with a list of quiz questions | Passed |
| `POST /summarise` | Valid text and max_bullets | HTTP 200 with summary and bullet_count | Passed |
| `POST /quiz` | `{"message":""}` | HTTP 422 because the required topic field is missing | Passed |
| `POST /summarise` | `{"message":""}` | HTTP 422 because the required text field is missing | Passed |

## Manual Swagger UI Tests

Open http://127.0.0.1:8000/docs.

### 1. Valid Request

Select `POST /chat`, click **Try it out**, and submit:

```json
{
  "message": "Explain what an API is"
}
```

Expected result: HTTP 200 with a JSON object containing `answer`, `source`, and `success`.

Actual result: Passed (HTTP 200).

### 2. Invalid Request

Select `POST /quiz` and submit:

```json
{
  "message": ""
}
```

Expected result: HTTP 422 because the required `topic` field is missing.

Actual result: Passed (HTTP 422).

### 3. Additional Validation Test

Select `POST /summarise` and submit:

```json
{
  "message": ""
}
```

Expected result: HTTP 422 because the required `text` field is missing.

Actual result: Passed (HTTP 422).

## Automated Tests

Run the following command from the project root:

```powershell
python -m pytest
```

The automated tests cover:
- Health endpoint response.
- Valid chat request.
- Invalid chat request.

**Test Results: 3 passed.**

## Conclusion

All four API endpoints were tested successfully using Swagger UI.

Valid requests returned HTTP 200, while invalid requests returned HTTP 422 validation errors.

All three automated tests passed successfully.

The chat, quiz, and summarisation endpoints currently use placeholder logic and do not require an external AI model.
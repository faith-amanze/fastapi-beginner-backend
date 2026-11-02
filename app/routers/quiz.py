from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(tags=["Quiz"])

class QuizRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=100)
    number_of_questions: int = Field(default=5, ge=1, le=10)

class QuizQuestion(BaseModel):
    question: str
    options: list[str]
    answer: str

class QuizResponse(BaseModel):
    topic: str
    questions: list[QuizQuestion]

@router.post("/quiz", response_model=QuizResponse)
def create_quiz(request: QuizRequest):
    # Placeholder questions demonstrate the required response structure.
    questions = [
        {
            "question": f"What is one important thing to know about {request.topic}?",
            "options": ["A basic concept", "An unrelated topic", "None of these"],
            "answer": "A basic concept",
        }
        for _ in range(request.number_of_questions)
    ]
    return {"topic": request.topic, "questions": questions}

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(tags=["Chat"])

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)

class ChatResponse(BaseModel):
    answer: str
    source: str
    success: bool

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Placeholder logic: replace this with an AI model later.
    return {
        "answer": f"You said: {request.message}",
        "source": "placeholder",
        "success": True,
    }

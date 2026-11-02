from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(tags=["Summarise"])

class SummariseRequest(BaseModel):
    text: str = Field(min_length=10, max_length=10000)
    max_bullets: int = Field(default=3, ge=1, le=10)

class SummariseResponse(BaseModel):
    summary: list[str]
    bullet_count: int

@router.post("/summarise", response_model=SummariseResponse)
def summarise(request: SummariseRequest):
    # Placeholder logic: split the input into sentences and take the requested number.
    parts = [part.strip() for part in request.text.replace("!", ".").replace("?", ".").split(".") if part.strip()]
    bullets = parts[:request.max_bullets] or [request.text[:160]]
    return {"summary": bullets, "bullet_count": len(bullets)}

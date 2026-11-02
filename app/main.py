from fastapi import FastAPI
from app.routers import health, chat, quiz, summarise

app = FastAPI(
    title="Beginner AI Assistant API",
    description="A small FastAPI backend with placeholder AI features.",
    version="1.0.0",
)

app.include_router(health.router)
app.include_router(chat.router)
app.include_router(quiz.router)
app.include_router(summarise.router)

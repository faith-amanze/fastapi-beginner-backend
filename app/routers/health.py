from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check():
    """Return API status without calling an AI model."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

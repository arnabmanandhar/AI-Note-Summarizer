from fastapi import APIRouter, HTTPException
from app.models import SummarizeRequest
from app.summarizer import summarize_text

router = APIRouter(prefix="/summarize", tags=["summarization"])

@router.post("/")
async def summarize(request: SummarizeRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text must not be empty")

    summary = summarize_text(
        text=request.text,
        max_length=request.max_length,
        min_length=request.min_length
    )
    return {"summary": summary}

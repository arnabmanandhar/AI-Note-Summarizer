from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=32)
def get_summarizer():
    """Load the T5 model once using caching to avoid reinitialization"""
    summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")    # Load the summarization pipeline
    return summarizer

def summarize_text(text: str, max_length: int = 100, min_length: int = 30) -> str:
    summarizer = get_summarizer()
    summary = summarizer(
        text, 
        max_length=max_length, 
        min_length=min_length, 
        do_sample=False
    )
    return summary[0]['summary_text']
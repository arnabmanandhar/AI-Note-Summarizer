from fastapi import FastAPI
from app.routers import summarize
from app.config import Settings

app = FastAPI(title="AI Note Summarization API", version="1.0.0")

# Load environment settings
settings= Settings()

# Include the summarization route
app.include_router(summarize.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Note Summarization API!"}
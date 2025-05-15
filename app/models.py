from pydantic import BaseModel, Field
from typing import Optional

class SummarizeRequest(BaseModel):
    text: str = Field(..., description="Text to summarize")
    max_length: Optional[int] = Field(25, description="Maximum length of the summary")
    min_length: Optional[int] = Field(15, description="Minimum length of the summary")

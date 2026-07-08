from pydantic import BaseModel, Field

from typing import Literal

class PromptRequest(BaseModel):
    prompt: str = Field(min_length= 3, max_length=500)


class GenerateResponse(BaseModel):
    game_html : str
    prompt : str
    status : Literal["pending", "completed", "failed"]

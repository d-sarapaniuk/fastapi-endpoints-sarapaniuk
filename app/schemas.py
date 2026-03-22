from pydantic import BaseModel, Field


class SumRequest(BaseModel):
    a: int
    b: int


class RepeatRequest(BaseModel):
    text: str = Field(min_length=1)
    times: int = Field(ge=1, le=10)
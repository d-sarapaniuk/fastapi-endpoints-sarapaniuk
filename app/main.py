from fastapi import FastAPI
from app.utils import calculate_sum, repeat_text
from app.schemas import SumRequest, RepeatRequest

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from main"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/sum")
def sum_values(payload: SumRequest):
    return {"result": calculate_sum(payload.a, payload.b)}


@app.post("/repeat")
def repeat_value(payload: RepeatRequest):
    return {"result": repeat_text(payload.text, payload.times)}
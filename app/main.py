from fastapi import FastAPI
from app.utils import calculate_sum, repeat_text

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/sum")
def sum_values(payload: dict):
    a = payload["a"]
    b = payload["b"]
    return {"result": calculate_sum(a, b)}


@app.post("/repeat")
def repeat_value(payload: dict):
    text = payload["text"]
    times = payload["times"]
    return {"result": repeat_text(text, times)}
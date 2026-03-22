import logging
from fastapi import FastAPI
from app.utils import calculate_sum, repeat_text
from app.schemas import SumRequest, RepeatRequest

app = FastAPI()
logging.basicConfig(level=logging.INFO)


@app.get("/")
def root():
    return {"message": "Hello from main branch"}


@app.get("/health")
def health():
    logging.info("Healthcheck called")
    return {"status": "ok"}


@app.post("/sum")
def sum_values(payload: SumRequest):
    logging.info(f"Calculating sum: {payload.a} + {payload.b}")
    return {"result": calculate_sum(payload.a, payload.b)}


@app.post("/repeat")
def repeat_value(payload: RepeatRequest):
    logging.info(f"Repeating text '{payload.text}' {payload.times} times")
    return {"result": repeat_text(payload.text, payload.times)}
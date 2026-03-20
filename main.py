from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(request: TextRequest):
    result = classifier(request.text)
    return {
        "text": request.text,
        "sentiment": result[0]['label'],
        "confidence": round(result[0]['score'], 4)
    }

@app.get("/")
def home():
    return {"message": "API-ul de Analiză de Sentiment este activ!"}
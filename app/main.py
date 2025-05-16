from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment import analyze_sentiment

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analyzer API"}

@app.post("/analyze")
def analyze(request: TextRequest):
    sentiment = analyze_sentiment(request.text)
    return {"sentiment": sentiment}

# Sentiment Analyzer API (FastAPI)

This is a simple FastAPI project that analyzes sentiment of a given sentence using TextBlob.

## 🔍 What It Does

Send a POST request with a sentence, and get a sentiment prediction: `positive`, `negative`, or `neutral`.

## ▶️ How to Run Locally

1. Clone the repo
```bash
git clone https://github.com/NibidaGhimire/fuse_assignment_1.git
cd fuse_assignment_1
```

Install requirements:
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

Virtual Environment (This is Optional)
```bash
python3 -m venv venv
source venv/bin/activate
```

Run the API
```bash
uvicorn app.main:app --reload
```


Test it!
```bash
Visit http://localhost:8000/docs
```

Run with Docker:
```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```


Running tests:
```bash
pytest
```




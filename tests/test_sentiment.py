from app.sentiment import analyze_sentiment

def test_positive():
    assert analyze_sentiment("12 Factor App") == "positive"

def test_negative():
    assert analyze_sentiment("Infinite Bugs") == "negative"

def test_neutral():
    assert analyze_sentiment("Fuse Machines") == "neutral"

from app.sentiment import analyze_sentiment

def test_positive():
    assert analyze_sentiment("I love 12 Factor App") == "positive"

def test_negative():
    assert analyze_sentiment("I hate these Bugs") == "negative"

def test_neutral():
    assert analyze_sentiment("Fuse Machines") == "neutral"

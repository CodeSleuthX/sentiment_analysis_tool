import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download("vader_lexicon")

# Initialize the vader sentiment analyzer
sid = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
  # Use Vader sentiment analyzer to get sentiment scores
  sentiment_score = sid.polarity_scores(text)

  # Determine the sentiment based on compound scores
  compound_scores = sentiment_scores["compound"]

  if compound_score >= 0.05:
    return "Positive"
  elif compound_score <= -0.05:
    return "Negative"
  else:
    return "Neutral"

if __name__ == "__main__":
  while True:
    user_text = input("Enter text (or type 'exit' to quit): ")

  if user_text.lower() == "exit":
    break

  sentiment = analyze_sentiment(user_text)
  print(f"Sentiment: {sentiment}")

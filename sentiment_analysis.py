import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Load the scraped news
df = pd.read_csv("scraped_news.csv")

# Check if required columns exist
if "headline" not in df.columns:
    print("❌ Error: 'headline' column not found in scraped_news.csv")
    exit()

# Apply sentiment analysis
def get_sentiment(text):
    scores = sia.polarity_scores(str(text))
    return scores["pos"], scores["neu"], scores["neg"], scores["compound"]

df[["positive", "neutral", "negative", "compound"]] = df["headline"].apply(lambda x: pd.Series(get_sentiment(x)))

# Save results
df.to_csv("sentiment_results.csv", index=False)
print("✅ Sentiment analysis completed. Data saved to sentiment_results.csv")

print(df.head())  # Print sample results to verify

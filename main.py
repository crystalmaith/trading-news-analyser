from scraper import get_news
from sentiment_analysis import analyze_sentiment

def main():
    news = get_news()
    
    print("🔹 Latest Financial News & Sentiment Scores 🔹")
    for item in news[:5]:  # Process first 5 headlines
        sentiment = analyze_sentiment(item['headline'])
        print(f"📰 {item['headline']}")
        print(f"🔗 {item['link']}")
        print(f"📊 Sentiment Score: {sentiment}\n")

if __name__ == "__main__":
    main()

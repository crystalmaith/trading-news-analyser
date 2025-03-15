import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment analysis results
df = pd.read_csv("sentiment_results.csv")

# Check if required columns exist
if "website" not in df.columns or "positive" not in df.columns:
    print("❌ Error: Required columns missing in sentiment_results.csv")
    exit()

# Fill missing values with 0
df.fillna(0, inplace=True)

# Count total articles per website
article_counts = df["website"].value_counts()

# Normalize sentiment scores (convert to percentage of total articles per source)
grouped = df.groupby("website")[["positive", "neutral", "negative"]].mean()
grouped["total_articles"] = article_counts

# Normalize based on article counts
grouped["positive"] *= 100
grouped["neutral"] *= 100
grouped["negative"] *= 100

# Plot sentiment distribution for all sources
plt.figure(figsize=(10, 6))
grouped[["positive", "neutral", "negative"]].plot(kind="bar", stacked=True, colormap="viridis", ax=plt.gca())
plt.title("Normalized Sentiment Analysis of Financial News by Source")
plt.xlabel("News Website")
plt.ylabel("Sentiment Score (Percentage)")
plt.xticks(rotation=45)
plt.legend(["Positive", "Neutral", "Negative"])
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save & show chart
plt.savefig("sentiment_analysis_chart.png")
plt.show()
print("✅ Visualization updated. Chart saved as sentiment_analysis_chart.png")

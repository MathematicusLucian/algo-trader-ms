from src.services.sentiment_service import TwitterSentiment

if __name__ == "__main__":
    sentimen_determinator = TwitterSentiment(True)
    tweet_content = sentimen_determinator.get_tweets()
    sentiment = sentimen_determinator.determine_sentiment(tweet_content)
    sentimen_determinator.print_sentiment(sentiment)
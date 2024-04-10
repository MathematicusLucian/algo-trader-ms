from src.utils import *
from src.services.sentiment_service import TwitterSentiment

if __name__ == "__main__":
    is_financial = is_arg("--f")
    sentiment_determinator = TwitterSentiment(is_financial)
    tweet_content = sentiment_determinator.get_tweets()
    sentiment = sentiment_determinator.determine_sentiment(tweet_content)
    sentiment_determinator.print_sentiment(sentiment)
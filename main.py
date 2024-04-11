# from src.utils import *
from src.services.sentiment_service import XSentimentService
from src.services.x_service import x_unofficial

if __name__ == "__main__":
    # is_financial = is_arg("--f")

    x_unofficial.scrape_tweets("@elonmusk")

    # sentiment_determinator = XSentimentService(is_financial)
    # tweet_content = sentiment_determinator.get_tweets()
    # sentiment = sentiment_determinator.determine_sentiment(tweet_content)
    # sentiment_determinator.print_sentiment(sentiment)
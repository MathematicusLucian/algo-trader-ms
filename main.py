from src.services.sentiment_service import XSentimentService
from src.services.x_service import XArchive
from src.services.crypto_analysis import *
from src.utils import *

if __name__ == "__main__":
    date_from = "2010-06-04" # 21:31:57" #BTC 2016-07-01
    date_to = "2021-04-11" # 18:50:33" #BTC 2024-03-12

    doge_hisoric_data = get_historic_data("DOGE", date_from, date_to)
    print(doge_hisoric_data)

    x_arxiv = XArchive()
    print(x_arxiv.get_historic_data_by_currency("elonmusk", "doge", date_from, date_to))

    # is_financial = is_arg("--f")
    # x_unofficial.scrape_tweets("@elonmusk")
    # sentiment_determinator = XSentimentService(is_financial)
    # tweet_content = sentiment_determinator.get_tweets()
    # sentiment = sentiment_determinator.determine_sentiment(tweet_content)
    # sentiment_determinator.print_sentiment(sentiment)
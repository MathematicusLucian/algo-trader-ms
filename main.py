import random
import wandb
from src.services.sentiment_service import XSentimentService
from src.services.x_service import XArchive
from src.services.crypto_analysis import *
from src.utils import *

if __name__ == "__main__":
    date_from = "2016-07-01"
    date_to = "2021-04-11"
    doge_hisoric_data = get_historic_data("DOGE", date_from, date_to)
    x_arxiv = XArchive()
    elon_doge_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "doge|dogecoin|Doge|Dogecoin", date_from, date_to)
    elon_btc_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "btc|bitcoin|BTC|Bitcoin", date_from, date_to)

    # wandb.init(
    #     project="my-awesome-project",
    #     config={
    #         "learning_rate": 0.02,
    #         "architecture": "CNN",
    #         "dataset": "CIFAR-100",
    #         "epochs": 10,
    #     }
    # )
    # epochs = 10
    # offset = random.random() / 5
    # for epoch in range(2, epochs):
    #     acc = 1 - 2 ** -epoch - random.random() / epoch - offset
    #     loss = 2 ** -epoch + random.random() / epoch + offset
    #     wandb.log({"acc": acc, "loss": loss})
    # wandb.finish()

    # is_financial = is_arg("--f")
    # x_unofficial.scrape_tweets("@elonmusk")
    # sentiment_determinator = XSentimentService(is_financial)
    # tweet_content = sentiment_determinator.get_tweets()
    # sentiment = sentiment_determinator.determine_sentiment(tweet_content)
    # sentiment_determinator.print_sentiment(sentiment)
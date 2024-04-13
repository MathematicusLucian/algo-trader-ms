import random
import wandb
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from src.services.sentiment_service import XSentimentService
from src.services.x_service import XArchive
from src.services.crypto_analysis import *
from src.utils import *

class color:
    BOLD = '\033[1m' + '\033[93m'
    END = '\033[0m'

if __name__ == "__main__":
    # run = wandb.init(project='bitcoin-musk', name='bitcoin_analysis')
    # is_financial = is_arg("--f")
    date_from = "2016-07-01"
    date_to = "2021-04-11"
    doge_hisoric_data = get_historic_data("DOGE", date_from, date_to)
    x_arxiv = XArchive()
    elon_doge_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "doge|dogecoin|Doge|Dogecoin", date_from, date_to)
    elon_btc_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "btc|bitcoin|BTC|Bitcoin", date_from, date_to)
    my_colors = ["#ce8f5a", "#efd199", "#80c8bc", "#5ec0ca", "#6287a2"]
    sns.palplot(sns.color_palette(my_colors))
    sns.set_style("white")
    mpl.rcParams['xtick.labelsize'] = 16
    mpl.rcParams['ytick.labelsize'] = 16
    mpl.rcParams['axes.spines.left'] = False
    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['axes.spines.top'] = False
    x_arxiv.convert_tweet_date_to_str(elon_doge_tweets)
    timestamps = elon_doge_tweets["date"]
    dgc_prices = doge_hisoric_data.sort_values("Date", ascending=False).head(90)
    dgc_prices["Date"] = dgc_prices["Date"].apply(lambda x: datetime.fromisoformat(x).timestamp())
    for k, tweet in enumerate(elon_doge_tweets["tweet"][:6]): print(color.BOLD + f"{k+1}." + color.END, tweet)
    # Get intersection
    x_values = dgc_prices[dgc_prices["Date"].isin(timestamps)]["Date"]
    y_values = dgc_prices[dgc_prices["Date"].isin(timestamps)]["Adj Close"]
    plt.figure(figsize = (25, 11))
    for x, y in zip(x_values, y_values):
        plt.scatter(x, y, color="#FF451D", lw=13, zorder=2)
    plt.plot(dgc_prices["Date"], dgc_prices["Adj Close"], color=my_colors[3], lw=3, zorder=1)
    plt.title("Dogecoin Price & Elon's Tweets", size=25)
    plt.xlabel("Time", size=20)
    plt.ylabel("$ Price", size=20);
    # x_unofficial.scrape_tweets("@elonmusk")
    # sentiment_determinator = XSentimentService(is_financial)
    # tweet_content = sentiment_determinator.get_tweets()
    # sentiment = sentiment_determinator.determine_sentiment(tweet_content)
    # sentiment_determinator.print_sentiment(sentiment)
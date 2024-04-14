import sys, os
from markupsafe import escape
import json
import random
import wandb
# import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from flask import abort, app, Blueprint, jsonify, redirect, render_template, request, url_for
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from src.utils import chart_colors
# from src.services.metals_data_service.gold_prices import fetch_gold_price
from src.services.sentiment_service import XSentimentService
# from src.services.x_service import XArchive, x_unofficial
from src.services.crypto_analysis import *
from src.strategy.SampleMM import SampleMM
from src.utils import *

algo_blueprint = Blueprint('blah', __name__)

# @algo_blueprint.errorhandler(404)
# def not_found():
#     return redirect(url_for('not_found'))

# @algo_blueprint('/not-found')
# def page_not_found(error):
#     abort(404)

@algo_blueprint.route("/")
def root():
    version = "v1"
    return "Algo API".format(escape(version))

@algo_blueprint.route('/mm', methods=['GET'])
def mm():
    strategy = SampleMM()
    strategy.run()
    return "mm"

# http://127.0.0.1:5000/gold/XAU/USD/today/
# @algo_blueprint.route('/gold/<base>/<symbol>/today', methods=['GET'])
# def gold_today(base, symbol):
#     now = datetime.now()
#     today = datetime.today()
#     data = fetch_gold_price(today, base, symbol)
#     # if data == None:
#     #     return redirect(url_for('not_found'))
#     return data

@algo_blueprint.route('/sentiment/<is_financial>', methods=['GET'])
def sentiment(is_financial):
    sentiment_determinator = XSentimentService(is_financial)
    tweet_content = sentiment_determinator.get_tweets()
    sentiment = sentiment_determinator.determine_sentiment(tweet_content)
    # sentiment_determinator.print_sentiment(sentiment)
    return sentiment

# @algo_blueprint.route('/scrape_tweets', methods=['GET'])
# def scrape_tweets():
#     return x_unofficial.scrape_tweets("@elonmusk")

# @algo_blueprint.route('/tweets_impact_on_crypto', methods=['GET'])
# def tweets_impact_on_crypto():
#     # run = wandb.init(project='bitcoin-musk', name='bitcoin_analysis')
#     # is_financial = is_arg("--f")
#     date_from = "2016-07-01"
#     date_to = "2021-04-11"
#     doge_hisoric_data = get_historic_data("DOGE", date_from, date_to)
#     x_arxiv = XArchive()
#     elon_doge_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "doge|dogecoin|Doge|Dogecoin", date_from, date_to)
#     elon_btc_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "btc|bitcoin|BTC|Bitcoin", date_from, date_to)
#     sns.palplot(sns.color_palette(chart_colors.LEGEND))
#     sns.set_style("white")
#     mpl.rcParams['xtick.labelsize'] = 16
#     mpl.rcParams['ytick.labelsize'] = 16
#     mpl.rcParams['axes.spines.left'] = False
#     mpl.rcParams['axes.spines.right'] = False
#     mpl.rcParams['axes.spines.top'] = False
#     x_arxiv.convert_tweet_date_to_str(elon_doge_tweets)
#     timestamps = elon_doge_tweets["date"]
#     dgc_prices = doge_hisoric_data.sort_values("Date", ascending=False).head(90)
#     dgc_prices["Date"] = dgc_prices["Date"].apply(lambda x: datetime.fromisoformat(x).timestamp())
#     for k, tweet in enumerate(elon_doge_tweets["tweet"][:6]): print(chart_colors.BOLD + f"{k+1}." + chart_colors.END, tweet)
#     # Get intersection
#     x_values = dgc_prices[dgc_prices["Date"].isin(timestamps)]["Date"]
#     y_values = dgc_prices[dgc_prices["Date"].isin(timestamps)]["Adj Close"]
#     plt.figure(figsize = (25, 11))
#     for x, y in zip(x_values, y_values):
#         plt.scatter(x, y, color="#FF451D", lw=13, zorder=2)
#     plt.plot(dgc_prices["Date"], dgc_prices["Adj Close"], color=chart_colors.LEGEND[3], lw=3, zorder=1)
#     plt.title("Dogecoin Price & Elon's Tweets", size=25)
#     plt.xlabel("Time", size=20)
#     plt.ylabel("$ Price", size=20)

@algo_blueprint.route('/y', methods=['POST'])
def y():
 return jsonify("blah blah")
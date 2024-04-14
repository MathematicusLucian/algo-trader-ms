import sys, os
from markupsafe import escape
import json
import random
from datetime import datetime
import pytz
from flask import abort, app, Blueprint, jsonify, redirect, render_template, request, url_for
from pandas import Timestamp
import wandb
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import AnnotationBbox, OffsetImage
# import seaborn as sns
from src.services.metals_data_service.gold_prices import fetch_gold_price
# from src.services.sentiment_service import XSentimentService
# from src.services.x_service import XArchive, x_unofficial
# from src.services.crypto_analysis import *
# from src.strategy.SampleMM import SampleMM
# from src.utils import *
# from src.utils import chart_colors

algo_blueprint = Blueprint('blah', __name__)

# @algo_blueprint.errorhandler(404)
# def not_found():
#     return redirect(url_for('not_found'))

# @algo_blueprint('/not-found')
# def page_not_found(error):
#     abort(404)

# http://127.0.0.1:5001/
@algo_blueprint.route("/")
def root():
    version = "v1.0.0"
    return "Algo API: " + format(escape(version))

# @algo_blueprint.route('/mm', methods=['GET'])
# def mm():
#     strategy = SampleMM()
#     strategy.run()
#     return "mm"

# http://127.0.0.1:5001/historic_values_today/USD/XAU/
@algo_blueprint.route('/historic_values_today/<base_curr>/<symbol>/', methods=['GET'])
def historic_values(base_curr, symbol):
    # today_timestamp = datetime.now().timestamp()
    # today = datetime.now()
    # iso_date = today.isoformat()
    # iso_date_with_hash = datetime.now().isoformat('#')
    # iso_date_with_space = today.isoformat()
    # today_datestring = datetime.today()
    # aware_us_central = datetime.now(pytz.timezone('US/Central'))
    # print('US Central DateTime', aware_us_central)
    # iso_date = aware_us_central.isoformat()
    # print('ISO Datetime', iso_date)
    data = fetch_gold_price("", base_curr, symbol)
    # if data == None:
    #     return redirect(url_for('not_found'))
    return jsonify(data)

# @algo_blueprint.route('/sentiment/<is_financial>', methods=['GET'])
# def sentiment(is_financial):
#     sentiment_determinator = XSentimentService(is_financial)
#     tweet_content = sentiment_determinator.get_tweets()
#     sentiment = sentiment_determinator.determine_sentiment(tweet_content)
#     # sentiment_determinator.print_sentiment(sentiment)
#     return sentiment

# # @algo_blueprint.route('/scrape_tweets', methods=['GET'])
# # def scrape_tweets():
# #     return x_unofficial.scrape_tweets("@elonmusk")

# # @algo_blueprint.route('/tweets_impact_on_crypto', methods=['GET'])
# # def tweets_impact_on_crypto():
# #     # run = wandb.init(project='bitcoin-musk', name='bitcoin_analysis')
# #     # is_financial = is_arg("--f")
# #     date_from = "2016-07-01"
# #     date_to = "2021-04-11"
# #     doge_hisoric_data = get_historic_data("DOGE", date_from, date_to)
# #     x_arxiv = XArchive()
# #     elon_doge_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "doge|dogecoin|Doge|Dogecoin", date_from, date_to)
# #     elon_btc_tweets = x_arxiv.get_historic_data_by_currency("elonmusk", "btc|bitcoin|BTC|Bitcoin", date_from, date_to)
# #     sns.palplot(sns.color_palette(chart_colors.LEGEND))
# #     sns.set_style("white")
# #     mpl.rcParams['xtick.labelsize'] = 16
# #     mpl.rcParams['ytick.labelsize'] = 16
# #     mpl.rcParams['axes.spines.left'] = False
# #     mpl.rcParams['axes.spines.right'] = False
# #     mpl.rcParams['axes.spines.top'] = False
# #     x_arxiv.convert_tweet_date_to_str(elon_doge_tweets)
# #     timestamps = elon_doge_tweets["date"]
# #     dgc_prices = doge_hisoric_data.sort_values("Date", ascending=False).head(90)
# #     dgc_prices["Date"] = dgc_prices["Date"].apply(lambda x: datetime.fromisoformat(x).timestamp())
# #     for k, tweet in enumerate(elon_doge_tweets["tweet"][:6]): print(chart_colors.BOLD + f"{k+1}." + chart_colors.END, tweet)
# #     # Get intersection
# #     x_values = dgc_prices[dgc_prices["Date"].isin(timestamps)]["Date"]
# #     y_values = dgc_prices[dgc_prices["Date"].isin(timestamps)]["Adj Close"]
# #     plt.figure(figsize = (25, 11))
# #     for x, y in zip(x_values, y_values):
# #         plt.scatter(x, y, color="#FF451D", lw=13, zorder=2)
# #     plt.plot(dgc_prices["Date"], dgc_prices["Adj Close"], color=chart_colors.LEGEND[3], lw=3, zorder=1)
# #     plt.title("Dogecoin Price & Elon's Tweets", size=25)
# #     plt.xlabel("Time", size=20)
# #     plt.ylabel("$ Price", size=20)

# @algo_blueprint.route('/y', methods=['POST'])
# def y():
#  return jsonify("blah blah")
import sys, os
from markupsafe import escape
import json
import random
import time
from datetime import datetime
import pytz
import threading
import traceback
from flask import abort, app, Blueprint, jsonify, redirect, render_template, request, url_for
from pandas import Timestamp
import wandb
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import AnnotationBbox, OffsetImage
# import seaborn as sns
# import logging
from okx.exceptions import OkxAPIException, OkxParamsException, OkxRequestException
from okx.MarketData import MarketAPI
from okx.PublicData import PublicAPI
# from src.services.market_data_service.WssMarketDataService import ChecksumThread, WssMarketDataService
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
    return jsonify({"Algo API" : format(escape(version))})

@algo_blueprint.route('/historic_candlesticks__crypto/<base_curr>/<symbol>/', methods=['GET'])
async def historic_candlesticks__crypto(base_curr, symbol):
    is_paper_trading=False
    market_api = MarketAPI(flag='0' if not is_paper_trading else '1', debug=False)
    instrID = f"{base_curr}-{symbol}-SWAP"
    return jsonify(market_api.get_history_candlesticks(instrID))

# strategy = SampleMM()
# # run = await strategy.run()
# # url = "wss://ws.okx.com:8443/ws/v5/public"
# # url = "wss://ws.okx.com:8443/ws/v5/public?brokerId=9999"
# # market_data_service = WssMarketDataService(url=url, inst_id="BTC-USDT-SWAP", channel="books")
# # await market_data_service.start()
# # await market_data_service.run_service()
# # check_sum = ChecksumThread(market_data_service)
# # print("check_sum",check_sum)
# # check_sum.start()
# # print(market_data_service)

# http://127.0.0.1:5001/historic_values_today/USD/XAU/
@algo_blueprint.route('/historic_values_today/<base_curr>/<symbol>/', methods=['GET'])
def historic_values(base_curr, symbol):
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
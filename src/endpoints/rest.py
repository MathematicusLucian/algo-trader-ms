import sys, os
from markupsafe import escape
import json
import random
from bidict import bidict
from functools import wraps
import time
from datetime import datetime
import pytz
import threading
import traceback
from flask import abort, app, Blueprint, jsonify, redirect, render_template, request, url_for
# from flask_cache import Cache
# from flask_login import current_user
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
from src.strategy.macd import determine_macd_crypto
# from src.services.sentiment_service import XSentimentService
# from src.services.x_service import XArchive, x_unofficial
# from src.services.crypto_analysis import *
# from src.strategy.SampleMM import SampleMM
# from src.utils import *
# from src.utils import chart_colors

algo_rest_blueprint = Blueprint('crypto_data_apis', __name__)

def create_okx_api(api, is_paper_trading):
    flag='0' if not is_paper_trading else '1'
    if api=="MarketAPI":
        return MarketAPI(flag, debug=False)
    elif api=="PublicAPI":
        return PublicAPI(flag, debug=False)
    
def get_root():
    return "Hello World"

# @algo_rest_blueprint.errorhandler(404)
# def not_found():
#     return redirect(url_for('not_found'))

# @algo_rest_blueprint('/not-found')
# def page_not_found(error):
#     abort(404)

# --------------------
# ------- ROOT -------
# --------------------
# http://127.0.0.1:5000/
@algo_rest_blueprint.route("/")
# @cache.cached(timeout=60)
def index():
    version = "v1.0.0"
    return jsonify({"Algo API" : format(escape(version))})

@algo_rest_blueprint.route("/ping")
def ping():
    return jsonify({"Algo API" : "ping"})

@algo_rest_blueprint.route("/2000")
def fetch_2000():
    with open('api_sample_data/user.json') as user_file:
        file_contents = user_file.read()
    parsed_json = json.loads(file_contents)
    return jsonify(parsed_json)

@algo_rest_blueprint.route("/audusd15m")
def fetch_audusd15m():
    with open('api_sample_data/audusd15m.json') as user_file:
        file_contents = user_file.read()
    parsed_json = json.loads(file_contents)
    return jsonify(parsed_json)

@algo_rest_blueprint.route("/audusd15m_")
def fetch_audusd15m_():
    with open('api_sample_data/audusd15m_.json') as user_file:
        file_contents = user_file.read()
    parsed_json = json.loads(file_contents)
    return jsonify(parsed_json)

# /// STRATEGIES ///

# --------------------
# ------- MACD -------
# --------------------
@algo_rest_blueprint.route('/macd_crypto/', methods=['GET'])
def macd_crypto():
    return determine_macd_crypto()

# /// CRYPTO DATA ///

# --------------------
# --- CANDLESTICKS ---
# --------------------
# http://127.0.0.1:5000/candlesticks__crypto_spot/BTC/USD/
# http://127.0.0.1:5000/historic_candlesticks__crypto_spot/ETH/USD/
@algo_rest_blueprint.route('/candlesticks__crypto_spot/<base_curr>/<symbol>/', methods=['GET'])
async def candlesticks__crypto_spot(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_candlesticks(instrID))

# http://127.0.0.1:5000/historic_candlesticks__crypto_spot/BTC/USD/
# http://127.0.0.1:5000/historic_candlesticks__crypto_spot/ETH/USD/
@algo_rest_blueprint.route('/historic_candlesticks__crypto_spot/<base_curr>/<symbol>/', methods=['GET'])
async def historic_candlesticks__crypto_spot(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_index_candlesticks(instrID))

@algo_rest_blueprint.route('/historic_candlesticks__crypto_mark_price/<base_curr>/<symbol>/', methods=['GET'])
async def historic_candlesticks__crypto_mark_price(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_mark_price_candlesticks(instrID))

# http://127.0.0.1:5000/historic_candlesticks__crypto_swap/BTC/USD/
# http://127.0.0.1:5000/historic_candlesticks__crypto_swap/ETH/USD/
# https://www.okx.com/docs-v5/en/#public-data-rest-api-get-index-candlesticks
@algo_rest_blueprint.route('/historic_candlesticks__crypto_swap/<base_curr>/<symbol>/', methods=['GET'])
async def historic_candlesticks__crypto_swap(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}-SWAP"
    return jsonify(okx_api.get_history_candlesticks(instrID))

# --------------------
# ---- COMPONENTS ----
# --------------------
@algo_rest_blueprint.route('/index_components/<base_curr>/<symbol>/', methods=['GET'])
async def index_components__crypto(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_index_components(instrID))

# --------------------
# -- EXCHANGE RATE ---
# --------------------
@algo_rest_blueprint.route('/exchange_rate/', methods=['GET'])
async def exchange_rate():
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    return jsonify(okx_api.get_exchange_rate())

# --------------------
# ---- ORDERBOOK -----
# --------------------
@algo_rest_blueprint.route('/orderbook/<base_curr>/<symbol>/', methods=['GET'])
async def orderbook(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_orderbook(instrID))

@algo_rest_blueprint.route('/orderbook_basic/<base_curr>/<symbol>/', methods=['GET'])
async def orderbook_basic(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_order_lite_book(instrID))

# --------------------
# ----- TICKER(S) ----
# --------------------
@algo_rest_blueprint.route('/index_tickers/<base_curr>/<symbol>/', methods=['GET'])
async def index_tickers(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_index_tickers(instId=instrID))

# --------------------
# ------ TRADES ------
# --------------------
@algo_rest_blueprint.route('/trades/<base_curr>/<symbol>/', methods=['GET'])
async def trades(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_trades(instrID))

@algo_rest_blueprint.route('/history_trades/<base_curr>/<symbol>/', methods=['GET'])
async def history_trades(base_curr, symbol):
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    instrID = f"{base_curr}-{symbol}"
    return jsonify(okx_api.get_history_trades(instId=instrID))

# --------------------
# ------ VOLUME ------
# --------------------
@algo_rest_blueprint.route('/volume/', methods=['GET'])
async def volume():
    okx_api = create_okx_api("MarketAPI", is_paper_trading=False)
    return jsonify(okx_api.get_volume())

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

# /// METALS ///

# --------------------
# ------ GOLD ------
# --------------------
# http://127.0.0.1:5000/historic_values_today/USD/XAU/
@algo_rest_blueprint.route('/historic_values_today/<base_curr>/<symbol>/', methods=['GET'])
def historic_values(base_curr, symbol):
    data = fetch_gold_price("", base_curr, symbol)
    # if data == None:
    #     return redirect(url_for('not_found'))
    return jsonify(data)

# @algo_rest_blueprint.route('/sentiment/<is_financial>', methods=['GET'])
# def sentiment(is_financial):
#     sentiment_determinator = XSentimentService(is_financial)
#     tweet_content = sentiment_determinator.get_tweets()
#     sentiment = sentiment_determinator.determine_sentiment(tweet_content)
#     # sentiment_determinator.print_sentiment(sentiment)
#     return sentiment

# # @algo_rest_blueprint.route('/scrape_tweets', methods=['GET'])
# # def scrape_tweets():
# #     return x_unofficial.scrape_tweets("@elonmusk")

# # @algo_rest_blueprint.route('/tweets_impact_on_crypto', methods=['GET'])
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

# @algo_rest_blueprint.route('/y', methods=['POST'])
# def y():
#  return jsonify("blah blah")

REST_URL = "https://www.okx.com"
WSS_URL = "wss://ws.okx.com:8443/ws/v5/business"

# GET / Candlesticks history (https://www.okx.com/docs-v5/en/?shell#order-book-trading-market-data-get-candlesticks-history)
# Retrieve history candlestick charts from recent years(It is last 3 months supported for 1s candlestick).
# Rate Limit: 20 requests per 2 seconds
# Rate limit rule: IP
CANDLES_ENDPOINT = "/api/v5/market/history-candles"
INTERVALS = bidict({
    "1s": "1s",
    "1m": "1m",
    "3m": "3m",
    "5m": "5m",
    "15m": "15m",
    "30m": "30m",
    "1h": "1H",
    "2h": "2H",
    "4h": "4H",
    "6h": "6Hutc",
    "8h": "8Hutc",
    "12h": "12Hutc",
    "1d": "1Dutc",
    "3d": "3Dutc",
    "1w": "1Wutc",
    "1M": "1Mutc",
    "3M": "3Mutc"
})
MAX_RESULTS_PER_CANDLESTICK_REST_REQUEST = 100

# Get system time (https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-system-time)
# Retrieve API server time.
# Rate Limit: 10 requests per 2 seconds
# Rate limit rule: IP
HEALTH_CHECK_ENDPOINT = "/api/v5/public/time"
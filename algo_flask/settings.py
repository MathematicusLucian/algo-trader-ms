# -*- coding: utf-8 -*-
import os

# api key credential
API_KEY = ""
API_KEY_SECRET = ""
API_PASSPHRASE = ""
IS_PAPER_TRADING = True

# market-making instrument
TRADING_INSTRUMENT_ID = "BTC-USDT-SWAP"
TRADING_MODE = "cross"  # "cash" / "isolated" / "cross"

# default latency tolerance level
ORDER_BOOK_DELAYED_SEC = 60  # Warning if OrderBook not updated for these seconds, potential issues from wss connection
ACCOUNT_DELAYED_SEC = 60  # Warning if Account not updated for these seconds, potential issues from wss connection

# risk-free ccy
RISK_FREE_CCY_LIST = ["USDT", "USDC", "DAI"]

# params yaml path
PARAMS_PATH = os.path.abspath(os.path.dirname(__file__) + "/params.yaml")

class Config(object):
    APPNAME = 'JobHunter Flask API'
    SUPPORT_EMAIL = ''
    VERSION = '1.0.0'
    APPID = 'job_hunter_ng_docker'
    SECRET_KEY = os.urandom(24)
    TESTING = False

class DevConfig(Config):
    DEBUG = True
    FLASK_ENV='development'
    PROFILE = True

class QAConfig(Config):
    DEBUG = False
    FLASK_ENV='qa'
    STAGING = True
    TESTING = True

class ProdConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'
    STAGING = False

config = {
    'development': DevConfig,
    'testing': QAConfig,
    'production': ProdConfig,
    'default': DevConfig
}
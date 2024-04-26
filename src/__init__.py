# -*- coding: utf-8 -*-
from flask import Flask
from src.utils.utils import save_dataframe
# from src.services.db.db import create_connection, is_table
from src.utils.common import register_blueprints
from settings import config
from .utils import *

save_dataframe = save_dataframe
# create_connection = create_connection
# is_table = is_table

# market data
order_books = {}
instruments = {}
tickers_container = []
mark_px_container = []

# position management
balance_and_position_container = []
account_container = []
positions_container = []

# order management
orders_container = []
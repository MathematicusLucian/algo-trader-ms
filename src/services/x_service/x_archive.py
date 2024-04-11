import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from src.utils import get_root_dir

class XArchive:
    def fetch_tweets_archive_data(self, handle):
        return pd.read_csv(f"{get_root_dir()}/backtesting_data/tweets/{handle}_tweets.csv")

    # def create_plotly(df):
    #     fig = go.Figure(data=[go.Candlestick(x=df.date,
    #                 open=df.open,
    #                 high=df.high,
    #                 low=df.low,
    #                 close=df.close)])
    #     fig.show()

    def get_min_date(self, df):
        return df.date.min()

    def get_max_date(self, df):
        return df.date.max()

    def get_range_for_number_of_days(self, df, days):
        return df.tail(days)
    
    def get_range_between_dates(self, df, date_from, date_to):
        return df.loc[date_from:date_to]
    
    def get_historic_data_by_currency(self, handle, currency, date_from, date_to):
        df = self.fetch_tweets_archive_data(handle)
        tweets = self.get_range_between_dates(df, date_from, date_to)
        return tweets[tweets["tweet"].str.contains(currency)].reset_index(drop=True)
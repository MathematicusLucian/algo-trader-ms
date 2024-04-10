import tweepy
import configparser
import pandas as pd

class Listener(tweepy.Stream):
    tweets = []
    limit = 1

    def on_status(self, status):
        self.tweets.append(status)
        # print(status.user.screen_name + ": " + status.text)
        if len(self.tweets) == self.limit:
            self.disconnect()

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']
    return api_key, api_key_secret, access_token, access_token_secret

def twitter_api_setup():
    api_key, api_key_secret, access_token, access_token_secret = get_config()
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def twitter_search():
    api = twitter_api_setup()
    keywords = '@veritasium'
    limit=300

    # tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)
    tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)
    # tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

    columns = ['User', 'Tweet']
    data = []
    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.full_text])
    df = pd.DataFrame(data, columns=columns)

    print(df)

def twitter_stream():
    api = twitter_api_setup()
    api_key, api_key_secret, access_token, access_token_secret = get_config()
    stream_tweet = Listener(api_key, api_key_secret, access_token, access_token_secret)
    # keywords = ['2022', '#python']
    users = ['MehranShakarami', 'veritasium']
    user_ids = []

    for user in users:
        user_ids.append(api.get_user(screen_name=user).id)

    stream_tweet.filter(follow=user_ids)
    # stream_tweet.filter(track=keywords)

    columns = ['User', 'Tweet']
    data = []

    for tweet in stream_tweet.tweets:
        if not tweet.truncated:
            data.append([tweet.user.screen_name, tweet.text])
        else:
            data.append([tweet.user.screen_name, tweet.extended_tweet['full_text']])

    df = pd.DataFrame(data, columns=columns)

    print(df)

def twitter_users():
    api = twitter_api_setup()
    user = 'veritasium'
    limit=300

    tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)
    # tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

    columns = ['User', 'Tweet']
    data = []
    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.full_text])
    df = pd.DataFrame(data, columns=columns)

    print(df)
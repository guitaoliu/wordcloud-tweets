import twint
import datetime
import langid
import time

from .config import (
    USER_LIST,
    DAYS,
    EXCLUDE_JA_KO,
    PROXY_HOST,
    PROXY_PORT,
    PROXY_TYPE,
)
from .logger import logger

def get_tweet(user_list,days,exclude_ja_ko,proxy_host,proxy_port,proxy_type):

    tweets = []
    tweets_user = []

    time_period = datetime.date.today() - datetime.timedelta(days=days)

    for user in user_list:
        c = twint.Config()
        c.Proxy_host=proxy_host
        c.Proxy_port=proxy_port
        c.Proxy_type=proxy_type
        c.Store_object = True
        c.Store_object_tweets_list = tweets_user
        c.Filter_retweets = True
        c.Username = user
        c.Hide_output = True
        c.Since = time_period.strftime("%Y-%m-%d")
        c.Until = datetime.date.today().strftime("%Y-%m-%d")
        twint.run.Search(c)
        logger.info(user + 'DONE!')
        tweets += tweets_user

    tweet_text = [tweet.tweet for tweet in tweets]
    if exclude_ja_ko:
        tweet_text_exclude_ja = [row for row in tweet_text if langid.classify(row)[0] not in 'jako']
        return tweet_text_exclude_ja
    return tweet_text

tweets = get_tweet(
    USER_LIST,
    DAYS,
    EXCLUDE_JA_KO,
    PROXY_HOST,
    PROXY_PORT,
    PROXY_TYPE,
)
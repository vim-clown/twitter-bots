import os, praw, tweepy
from pytwitter import Api
from twitter import Twitter, OAuth
    

""" ------------BEGIN JOKE------------ """
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token_key = os.environ["access_token_key"]
access_token_secret = os.environ["access_token_secret"]
XAuth = Twitter(auth=OAuth(access_token_key, access_token_secret, consumer_key, consumer_secret))    
print("Intra auth")


hide_greentext_credits = Api(
consumer_key=os.environ["CONSUMERKEY"],
consumer_secret=os.environ["CONSUMERSECRET"],
access_token=os.environ["ACCESSTOKEN"],
access_secret=os.environ["ACCESSTOKENSECRET"],)
# Twitter Authentication
CONSUMERKEY = os.environ["CONSUMERKEY"]
CONSUMERSECRET = os.environ["CONSUMERSECRET"]
ACCESSTOKEN = os.environ["ACCESSTOKEN"]
ACCESSTOKENSECRET = os.environ["ACCESSTOKENSECRET"]
auth1 = tweepy.OAuth1UserHandler(CONSUMERKEY, CONSUMERSECRET)
auth1.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)
greentext_api = tweepy.API(auth1, wait_on_rate_limit=True)
# Reddit Authentication
reddit_read_only = praw.Reddit(
user_agent=os.environ["user_agent"],
client_id=os.environ["client_id"],
client_secret=os.environ["client_secret"],)
# Target sub-reddit
sub_reddit = reddit_read_only.subreddit("greentext")
print("Greentext auth")



hide_history_credits = Api(
consumer_key=os.environ["CONSUMER_KEY"],
consumer_secret=os.environ["CONSUMER_SECRET"],
access_token=os.environ["ACCESS_TOKEN"],
access_secret=os.environ["ACCESS_TOKEN_SECRET"],)
# Twitter Authentication
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
history_api = tweepy.API(auth, wait_on_rate_limit=True)
# Reddit Authentication
reddit_read_only = praw.Reddit(
user_agent=os.environ["user_agent1"],
client_id=os.environ["client_id1"],
client_secret=os.environ["client_secret1"],)
# Target sub-reddit
subreddit = reddit_read_only.subreddit("HistoryMemes")
post_dict = {}
print("HistoryMemes auth")



c_CONSUMERKEY = os.environ["capi_key"]
c_CONSUMERSECRET = os.environ["capi_key_secret"]
c_ACCESSTOKEN = os.environ["caccess_token"]
c_ACCESSTOKENSECRET = os.environ["caccess_token_secret"]
c_auth1 = tweepy.OAuth1UserHandler(c_CONSUMERKEY, c_CONSUMERSECRET)
c_auth1.set_access_token(c_ACCESSTOKEN, c_ACCESSTOKENSECRET)
credits_api = tweepy.API(c_auth1, wait_on_rate_limit=True)
print("credit bot auth")


""" ------------END JOKE------------ """

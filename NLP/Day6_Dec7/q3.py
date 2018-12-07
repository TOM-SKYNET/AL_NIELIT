"""
	3. Take tweets from FIFACom or one of your choice and display 10 tweets.
"""

import tweepy
from textblob import TextBlob;

consumer_key = "ldIf3h1MgqMhDXOnZOaAhpqcP"
consumer_secret = "tQlKsL6gNwS34ch95FuQ3M7bsbIPZsx39l3GNbAvqOIKb5lLLI"
access_token = "778782906403741696-dfSLfONoM5RgQEBe4B4UyEdercNIWxi" 
access_token_secret = "pKS0PJEUm86xBCbq4I4w8opM8rnd6FszvVdGOpMqBISXp"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline("@FIFAWorldCup")

for tweet in public_tweets:
	print tweet.text



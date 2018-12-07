"""
	3. Take tweets from FIFACom or one of your choice and display 10 tweets.
	4. Modify the above program and Classify if each tweet is Positive, Negative , Neutral.
"""

import tweepy
from textblob import TextBlob;

consumer_key = "ldIf3h1MgqMhDXOnZOaAhpqcP"
consumer_secret = "tQlKsL6gNwS34ch95FuQ3M7bsbIPZsx39l3GNbAvqOIKb5lLLIxxx"
access_token = "778782906403741696-dfSLfONoM5RgQEBe4B4UyEdercNIWxixxx" 
access_token_secret = "pKS0PJEUm86xBCbq4I4w8opM8rnd6FszvVdGOpMqBISXpxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline("@FIFAWorldCup")

for tweet in public_tweets:
	t1 = TextBlob(tweet.text);
	if t1.sentiment.polarity > 0 :
		print("Positive", t1);
	if t1.sentiment.polarity < 0 :
		print("Negative", t1);
	if t1.sentiment.polarity == 0 :
		print("Neutral", t1);





"""
	3. Take tweets from FIFACom or one of your choice and display 10 tweets.
"""

import tweepy
from textblob import TextBlob;

consumer_key = "ldIf3h1MgqMhDXOnZOaAhpqcP"
consumer_secret = "tQlKsL6gNwS34ch95FuQ3M7bsbIPZsx39l3GNbAvqOIKb5lLLI1111"
access_token = "778782906403741696-dfSLfONoM5RgQEBe4B4UyEdercNIWxi1111" 
access_token_secret = "pKS0PJEUm86xBCbq4I4w8opM8rnd6FszvVdGOpMqBISXp111"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

posCount = 0;
negCount = 0;
neuCount = 0;
public_tweets = api.user_timeline("@FIFAWorldCup")
for tweet in public_tweets:
	t1 = TextBlob(tweet.text);
	if t1.sentiment.polarity > 0 :
		posCount = posCount + 1;
	if t1.sentiment.polarity < 0 :
		negCount = negCount + 1;
	if t1.sentiment.polarity == 0 :
		neuCount = neuCount + 1;

print("Positive " + str(posCount));
print("Negative " + str(negCount));
print("Neutral " + str(neuCount));




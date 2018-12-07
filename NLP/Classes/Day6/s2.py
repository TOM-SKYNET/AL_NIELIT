import tweepy
from textblob import TextBlob;

consumer_key = "ZBwOwhgkJARnF3lZJJ0KprkpG"
consumer_secret = "M3VnIt4imF1WgbUD2pkDGclwOuoxRMTXVChiNOKwaYljfKXbhv"
access_token = "140781874-e0Rd5ndktwNuaVeDfl7PD3WsJqVVjQwxCiN36oEN" 
access_token_secret = "YNkbncE6Ae4SrjKEAIt617I5jgJjddmSoOoj8HkxGhPO1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


posCount = 0;
negCount = 0;
neuCount = 0;
public_tweets = api.user_timeline("@Outlookindia")
for tweet in public_tweets:
	t1 = TextBlob(tweet.text);
	if t1.sentiment.polarity > 0 :
#		print("Positive");
		posCount = posCount + 1;
	if t1.sentiment.polarity < 0 :
#		print("Negative");
		negCount = negCount + 1;
	if t1.sentiment.polarity == 0 :
#		print("Neutral");
		neuCount = neuCount + 1;

print("Positive " + str(posCount));
print("Negative " + str(negCount));
print("Neutral " + str(neuCount));




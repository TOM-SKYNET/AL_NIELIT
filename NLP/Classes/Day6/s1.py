from textblob import TextBlob;

s1 = "Jill is a bad girl";
t1 = TextBlob(s1);
if t1.sentiment.polarity > 0 :
	print("Positive");
if t1.sentiment.polarity < 0 :
	print("Negative");
if t1.sentiment.polarity == 0 :
	print("Neutral");

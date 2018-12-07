"""
	2. If the subjectivity is 0.0 display "It is a Fact"
	    If the subjectivity is not 0 , if the polarity lies between 0 and 1 display "Positive", 
	    if the polarity lies between -1 and 0 display "Negative", if the polarity is equal to 0 display "Neutral".
"""
from textblob import TextBlob

t1 = TextBlob("I am too bad")
print t1.sentiment

if t1.sentiment.subjectivity == 0:
	print 'It s a fact'
else:
 	print 'It s an Attitude'

if t1.sentiment.polarity == 0:
	print 'This is Neutral statement'
elif t1.sentiment.polarity > 0:
	print 'This is Postive statement '
elif t1.sentiment.polarity < 0:
	print 'This is Negative statement '

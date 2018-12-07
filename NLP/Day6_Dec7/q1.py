"""
	1. Take a sentence as input. Display  the Subjectivity and the Polarity of the statement.
"""

from textblob import TextBlob

t1 = TextBlob("I am too bad")
print t1.sentiment
"""
	1.  Have a list of minimum 5 sentences. Find how close they are to a query string using tfidfVectorizer and cosine_similarity.
"""

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

print ("\nCalculating document similarity scores...")

# Open and read a bunch of files 
s1="the seas are blue"
s2="the sun have planets"
s3="the sun is bright"
s4="sun has a boy"

# Create a string to use to test the similarity scoring

train_string = 'citizen machane'

# Construct the training set as a list
train_set = [train_string, s1,s2,s3,s4]

# Set up the vectoriser, passing in the stop words
tfidf= TfidfVectorizer()

# Apply the vectoriser to the training set
tfidf_matrix_train = tfidf.fit_transform(train_set)

# Print the score
print "\nSimilarity Score [*] ",cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train)

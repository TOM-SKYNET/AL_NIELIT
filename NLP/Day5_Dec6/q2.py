"""
	1.  Have a list of minimum 5 sentences. Find how close they are to a query string using tfidfVectorizer and cosine_similarity.

	2. Modify the program to read strings from files.
"""
# importing packages
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

print ("\nCalculating document similarity scores...")

# Open and read a bunch of files 
f = open('text.txt')
doc1 = str(f.read())

# Create a string to use to test the similarity scoring
train_string = "By these proceedings for judicial review the Claimant seeks to challenge the decision of the Defendant dated the 23rd of May 2014 refusing the Claimant's application of the 3rd of January 2012 for naturalisation as a British citizen"

# Construct the training set as a list
train_set = [train_string, doc1]

# Set up the vectoriser, passing in the stop words
tfidf_vectorizer = TfidfVectorizer()

# Apply the vectoriser to the training set
tfidf_matrix_train = tfidf_vectorizer.fit_transform(train_set)

# Print the score
print "\nSimilarity Score [*] ",cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train)
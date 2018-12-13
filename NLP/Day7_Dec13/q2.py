"""
	Create a few sentences . Find the frequency count of the words in the vocabulary.
	2. Cluster the words in the sentences  based on the count.
	4. Visualise the results.
"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
"Browsers help us to search for information",
"Games refresh our minds",
"Chrome is a Browser",
"Football is an interesting Game",
"Cricket is also an interesting Game",
"You can open many tabs in Browsers"]

tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(documents)
dict = tfidf.vocabulary_
print tfidf.vocabulary_
counts = dict.values()

length = len(dict.keys())
x_lab = []
for key in dict.keys():
	x_lab.append(key)

print 'Length :', length
wordsArr = np.arange(0,length)

model = KMeans(n_clusters=length);
X = list(zip(wordsArr, counts))
model.fit(X)

plt.scatter(wordsArr,counts,c=model.labels_)
#plt.xlabel("Words")
plt.ylabel("Occurance")
plt.xticks(counts, x_lab, rotation=90)
plt.show()

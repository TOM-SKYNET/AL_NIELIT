from sklearn.cluster import KMeans;
import matplotlib.pyplot as py;
from sklearn.feature_extraction.text import TfidfVectorizer;

students = ["Jack","Jill","Anu","Binu","Cinu","Emu"];

tfidf = TfidfVectorizer(stop_words='english');
tfidf.fit(students);
print(tfidf.vocabulary_);


print("Vocabulary");
dict = tfidf.vocabulary_;
print(dict.keys());
print(dict.values());

for value in dict.values():
	print(value);


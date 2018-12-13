from sklearn.cluster import KMeans;
import matplotlib.pyplot as py;
from sklearn.feature_extraction.text import TfidfVectorizer;

students = ["Jack","Jill","Anu","Binu","Cinu","Emu"];

tfidf = TfidfVectorizer(stop_words='english');
tfidf.fit(students);
dict = tfidf.vocabulary_;
studentNos = dict.values();

marks = [90,92,78,45,23,56];

model = KMeans(n_clusters=3);
X = list(zip(studentNos,marks));
model.fit(X);
print(model.labels_);

leng = len(students)
for x in range(0,leng) :
	print(str(students[x]) + " " + str(marks[x]) + " " + str(model.labels_[x]));

py.scatter(students,marks,c=model.labels_);
py.show();

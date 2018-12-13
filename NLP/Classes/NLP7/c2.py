from sklearn.cluster import KMeans;
import matplotlib.pyplot as py;


students = [1,2,3,4,5,6];
marks = [90,92,78,45,23,56];

model = KMeans(n_clusters=3);
X = list(zip(students,marks));
model.fit(X);
print(model.labels_);

leng = len(students)
for x in range(0,leng) :
	print(str(students[x]) + " " + str(marks[x]) + " " + str(model.labels_[x]));

py.scatter(students,marks,c=model.labels_);
py.show();

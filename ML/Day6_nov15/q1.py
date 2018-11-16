from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix

# image data set
data = load_digits()
X = data.images
y = data.target


n = len(data.images)
#print n
X = X.reshape(n,-1)

print X
X_train = X[:n//2]
y_train = y[:n//2]
X_test = X[n//2:]
y_test = y[n//2:]

model = SVC(gamma=0.001)
model.fit(X_train,y_train)
p = model.predict(X_test)

print "Confusion Matrix:", confusion_matrix(y_test,p)
print classification_report(y_test,p)

imglabels = list(zip(data.images,y))

for index, (image, label) in enumerate(imglabels[:8]):
    plt.subplot(2,4, index+1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation ='nearest')
    plt.title(label)
plt.show()

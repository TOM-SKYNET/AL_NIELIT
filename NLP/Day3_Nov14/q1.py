from textblob.classifiers import NaiveBayesClassifier

f = open("q1_text.txt","r")
data = f.readline().strip()
trainData = []
while data:
    splitData = data.split(',')
    category = splitData[0]
    content = splitData[1]
    tuple = content, category
    trainData.append(tuple)
    data = f.readline().strip()

cModel = NaiveBayesClassifier(trainData)
cat = cModel.classify("Bacterial Infections and Mycoses")
print "Category:", cat

f = open("testset.txt")
testData = f.read()

if cModel.classify(testData) == "C01":
    print "Bacterial Infections and Mycoses"
if cModel.classify(testData) == "C02":
    print "Virus Diseases"
        

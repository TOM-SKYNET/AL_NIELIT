from textblob.classifiers import NaiveBayesClassifier
import glob2

data =[]
for filename in glob2.glob("/home/ai29/Desktop/Programming/NLP/ay3_nov14/Assignment4/*/*", recursive=True):
    #print(filename)
    file = filename.split("/")[-2]
    d = open(filename)
    w = d.read().replace("\n","")    
    x = (w,filename)
    data.append(x)

print 'length:' , len(data)
#print data

model = NaiveBayesClassifier(data)
f = open("./Assignment 3/CategoryDescription.txt")
testData = f.read()
print testData

if model.classify(testData) == "C01":
    print 'Bacterial Infections and Mycoses'
if model.classify(testData) == "C02":
    print 'Virus Diseases'
if model.classify(testData) == "C03":
    print 'Parasitic Diseases'
if model.classify(testData) == "C04":
    print 'Neoplasms'
if model.classify(testData) == "C05":
    print 'Musculoskeletal Diseases'
if model.classify(testData) == "C06":
    print 'Digestive System Diseases'
if model.classify(testData) == "C07":
    print 'Stomatognathic Diseases'
if model.classify(testData) == "C08":
    print 'Respiratory Tract Diseases'
if model.classify(testData) == "C09":
    print 'Otorhinolaryngologic Diseases'
if model.classify(testData) == "C10":
    print 'Nervous System Diseases '

    

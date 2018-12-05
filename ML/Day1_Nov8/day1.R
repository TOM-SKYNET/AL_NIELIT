
# import package for Machine Learning using SKLEARN 
library(caret)
library(e1071)

##################################  Day 1 Questions  ###########################

#1. Prepare an ML model using KNN Classifier to predict the Species information for
#a given iris flower using Sepal Length, Sepal Width, Petal Length & Petal Width. Use
#the complete iris dataset for training. Use it to predict the species of an iris flower.

dataset <- iris
dataset
head(dataset)

fit.knn <- train(Species~., data=dataset, method="knn")
predict(fit.knn,dataset[1,(1:4)])

v <- createDataPartition(dataset$Species,p=.8, list=FALSE)
v
trainset <- dataset[v,]
testset <- dataset[-v,]
trainset
testset

# 2. Print the Accuracy Score and Confusion matrix for KNN Classifier using iris data.
# (Split iris dataset to train and test sets.) 
fitknn <- train(Species~.,data=trainset, method="knn")
predictions <- predict(fitknn,testset)
confusionMatrix(testset[,5],predictions)

# 3. Use the EColi dataset from the UCI Machine Learning data repository# 
# (https://archive.ics.uci.edu/ml/datasets.html), to develop a K Nearest Neigbour
# predictor to predict the class information (the last column in the dataset)

ecolidata = read.table('/home/ai29/Desktop/common/ML/Day1/Questions/ecoli.txt', head=TRUE)
ecolidata
#ecolitraindata = subset(ecolidata, -c("AAT_ECOLI")) # or ecolidata[,-1]
ecolitraindata <-ecolidata[,-1]
ecolitraindata

v1 <- createDataPartition(ecolitraindata[,8],p=.9, list=FALSE)
v1
length(v1)
trainset1 <- ecolitraindata[v1,]
testset1 <- ecolitraindata[-v1,]
trainset1
testset1
# Train the model and predictions
fitknn1 <- train(cp~.,data=trainset1, method="knn")
predictions <- predict(fitknn1,testset1)
confusionMatrix(testset1[,8],predictions)


# 4. Identify a suitable dataset from your area of interest for a classification problem.
# Develop an ML model to do prediction.

data = read.csv('/home/ai29/Desktop/Programming/ML/data/dataR2.csv')
data
v2 <- createDataPartition(data[,10],p=.8, list=FALSE)
v2
length(v2)
trainset2 <- data[v2,]
testset2 <- data[-v2,]
trainset2
testset2
# Train the model and predictions
fitknn2 <- train(Classification~.,data=trainset2, method="knn")
predictions <- predict(fitknn2,testset2)
confusionMatrix(data[,10],predictions)


library(caret)
library(e1071)

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

fitknn <- train(Species~.,data=trainset, method="knn")
predictions <- predict(fitknn,testset)
confusionMatrix(testset[,5],predictions)

#

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


fitknn1 <- train(cp~.,data=trainset1, method="knn")
predictions <- predict(fitknn1,testset1)
confusionMatrix(testset1[,8],predictions)

data = read.csv('/home/ai29/Desktop/Programming/ML/data/dataR2.csv')
data
v2 <- createDataPartition(data[,10],p=.8, list=FALSE)
v2
length(v2)
trainset2 <- data[v2,]
testset2 <- data[-v2,]
trainset2
testset2

fitknn2 <- train(Classification~.,data=trainset2, method="knn")
predictions <- predict(fitknn2,testset2)
confusionMatrix(data[,10],predictions)
?train

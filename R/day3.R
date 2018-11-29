
#Q1
student<-list(Name="Tom",RollNumber= 112, Gender="Male",Marks = c(45,46,47,48,48))
student
#dimnames(student)<-c("Name","RollNumber","Gender","Marks")

# Q1 a
avg = sum(as.numeric(unlist(student[4])))/5
avg

# Q1 b
roll_marks <- student[c(2,4)]
roll_marks

# Q1 c
student[[4]][5] = 100
student

#Q1 d & e
names = c("English","Maths","Chemistery","Physics","Biology")
names

student = list(student,names)
student

#Q 2
A = matrix(1:4, nrow = 2, ncol = 2, byrow = TRUE)
A
B = 2 * A
B

# Q 3
A = matrix(c(c(1,1,3), c(5,2,6), c(-2,-1,-3)), nrow = 3, ncol =3 , byrow = TRUE)
A
A3 <- A %*% A %*% A
A3

#Q4 
A = matrix(c(10,-10,10), nrow = 15, ncol = 3, byrow=TRUE)
A
T_A = t(A)
T_A %*% A

# 5 a b c
A = matrix(1:15, nrow = 3, ncol=5)
A
dimnames(A) = list(c("Alice","Bill","Sara"), c("P1","P2","P3","P4","P5"))
A
# Calculate the mean for all columns
m = mean(A)
m

# Q6
x = c(rep("macbook", 10), rep("mobile",15), rep("tablets", 5))
category = factor(x)
category
summary(category)



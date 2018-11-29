# 1) Obtain the result of 
# a. 3 X 4
# b. (8/2)???(3 X 4) 
# c. 8/(2???3) X 4 
# Use the short cut Control + Enter to execute the program 

3*4
(8/2)-(3*4)
(8/(2-3))*4

# 2) Create the number sequence:
#   (a) 1, 2, 3, . . . , 19, 20
#   (b) 20, 19, . . . , 2, 1
x<-1:20
x
y<-20:1
y

# 3) Use the function paste to create the following character vectors of length 30. 
#    "label 1", "label 2", ....., "label 30"

label<-"label"
num<-1:30
paste(label,num)

# 4) Store the string ???The quick brown fox jumps over the lazy dog??? into a variable.
#   a) In the string, replace the word ???brown??? with ???red???
#   b) Use substr() function to pick the word ???fox??? from the string
str1<-"The quick brown fox jumps over the lazy dog"
# Q 4 -a
sub('brown','red',str1)

# Q 4 -b
substr(str1,17,19)

# Q 5
b <- 3
h <- 4
p<-2*(b+h)
p

# Q 6
#rep(1:4,c(2,1,2,1))
#rep(1:4, each=2, len=10)
rep(c(4,6,3), each=1, times=10)


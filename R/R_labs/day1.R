# Q 1
3*4
(8/2-(3*4))
8/(2-3)*4

#Q 2
x<-1:20
y<-20:1

# Q 3
label<-"label"
num<-1:30
paste(label,num)

# Q 4
str1<-"The quick brown fox jumps over the lazy dog"
# Q 4 -a
sub('brown','red',str1)

# Q 4 -b
#substr(str1,14,nchar('fox'))
substr(str1,17,19)

# Q 5
b <- 3
h <- 4
p<-2*(b+h)
p

# Q 6
?rep()
#rep(1:4,c(2,1,2,1))
#rep(1:4, each=2, len=10)
rep(c(4,6,3), each=1, times=10)


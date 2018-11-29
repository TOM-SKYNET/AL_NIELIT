#  Q 1
x<-1:20
y<-19:1
v<-c(x,y)
v
v<-c(4,6,3)
v

# Q 2
x1<-seq(10,40,5)
v1<-v[c(4,6,3)]
v1
# base vector
v2<-c(4,6,3)

v3<-rep(v2,10)
v3
v4<-c(rep(v2,20, length.out=31))
v4

#v5<-c(rep(v2, times =3, length.out=NA, each=2))
v5<-c(rep(4,10),rep(6,20),rep(3,30))
v5

# Q 3
r<-c(2.27, 1.98, 1.69, 1.88, 1.64, 2.14)
h<-c(8.28, 8.04, 9.06, 8.70, 7.58, 8.34)
vol<-((1/3)*pi*(r^2)*h)
vol
vol1<-round(vol,2)
vol1
min(vol)
max(vol)

# Q 4
A<-sample(0:999,250)
A
B<-A[which(A>900)]
B
sort(B)

# Q 5 
heights<-c(180, 165, 160, 193)
weights<-c(87, 58, 65, 100)
h_in_meters<-heights/100
bmi<-weights/(h_in_meters^2)
bmi
bmi_l_25<-bmi[which(bmi>25)]
bmi_l_25
avg_bmi=mean(bmi)
avg_bmi

# Q 6 
marks <- c(sample(50:100,10, replace =TRUE))
marks
p1 <- mean(marks)
p1
p2 <- median(marks)
p2


# Q 7
dry <- c(77, 93, 92, 68, 88, 75, 100)
sum(dry)
length(dry)
mean(dry)
sum(dry)/length(dry)
sort(dry)
median(dry)
sd(dry)
var(dry)
sd(dry)^2
min(dry)
max(dry)
summary(dry)


# Q 8
n<-sample(1:20,10, replace=TRUE)
n
n1 <- n[which(n%%2 ==0)]
n1




# Q1
a= sample(1:6,3000, replace=TRUE)
c= sample(30:70,27, replace=TRUE)
p = sample(c("H","T"), 1000, replace=TRUE)

n= rnorm(100,0,30)
pn = dnorm(n,0,30)
plot(n,pn)

cn= pnorm(n,0,30)
plot(n,cn)

qnorm(0.2,0,30)
qnorm(0.5,0,30)

n1 = rnorm(100,0,15)
p1 = dnorm(n1,0,15)
plot(n1,p1)

# Q3
n2 = rnorm(100,0,45)
p2 = dnorm(n2,0,45)
plot(n2,p2)

n3 = rnorm(100,50,30)
p3 = dnorm(n3,50,30)
plot(n3,p3)

n4 = rnorm(100,-50,30)
p4 = dnorm(n4,-50,30)
plot(n3,p3)

# Q4
x = rnorm(5000,20,5)
k = dnorm(x,20,5)
hist(k)

# Q5 
a = 1- pnorm(29,22,5)
a
b = pnorm(17,22,5)
b
c = pnorm(15,22,5)
c
d = c + (1-pnorm(25,22,5))
d


# Q6 (Hint: 1/(sqrt(2*pi)*sigma)*exp(-((31 - mu)^2/(2*sigma^2))))
mu = 30
sigma = 2
var =4
f = 1/(sqrt(2*pi)*sigma)*exp(-((31 - mu)^2/(2*sigma^2)))
f


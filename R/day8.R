
# Q1
dbinom(5,50,0.8)
dbinom(5,50,0.5)

pbinom(5,50,.8)
1-pbinom(5,50,.5)

# Q 2
dbinom(40,60,0.65)
1-dbinom(40,60,0.65)

# Q 3
x = seq(0,30,by=1)
y = dbinom(x,30,0.15)
plot(x,y)

x = seq(0,30,by=1)
y = dbinom(x,30,0.4)
plot(x,y)

x = seq(0,30,by=1)
y = dbinom(x,30,0.8)
plot(x,y)

# Q4
# a) 20,25 or 30 times
sum(dbinom(c(20,25,30),60,0.5))
# b) less than 20 times
pbinom(19,60,.5)
# between 20 and 30 times
pbinom(30,60,.5)-pbinom(20,60,0.5)

# Q 5, 
b = rpois(100,lambda = .5)
b
hist(b)
b = rpois(100,lambda = 1.5)
b
hist(b)
b = rpois(100,lambda = 5)
b
hist(b)

#
# Q6 
a = rpois(2608, lambda=10097/2608)
hist(a)

# Q7
# a. X is less than 5
ppois(5,7)
# b. X is greater than 10
1-ppois(10,7)
# c. X is between 4 and 16
ppois(16,7) -ppois(4,7)

# Q8
punif(6,0,25)
?punif



# Day6 31 Oct 2018 Quetions 9

# Q 1:
age = c(2,3,5,7,8)
weight = c(14,20,32,42,44)
relation = lm(weight~age)
#relation
plot(age,weight)
abline(relation)
k = data.frame(age=6)
predict(relation,k) # perdicted value
plot(age,weight)
a = lm(age~weight)
a
abline(lm(age~weight))


# Q 2 
x = c(8,7,6,4,2,1)
y = c(15,19,25,23,34,40)
r  = cor(x,y)
r
rel = lm(x~y)
m = data.frame(y=2)
predict(rel,m)

rel1 = lm(y~x)
m1 = data.frame(x=5)
predict(rel1,m1)

# Q 3
x = c(6,4,8,5,3.5) # maths
y = c(6.5,4.5,7,5,4) # chemistry
rel3 = lm(y~x)
plot(x,y)
abline(rel3)
df = data.frame(x=7.5)
predict(rel3,df)

# Q 4
x = c(186,189,190,192,193,193,198,201,203,205) # heights in cms
y = c(85,85,86,90,87,91,93,103,100,101) # weights in Kilograms
rel4 = lm(y~x)
plot(x,y)
abline(rel4)
c = cor(x,y)
c
rel5 = lm(y~x)
k = data.frame(x=208)
predict(rel5,k)

# Q 5 #80 
# Q 5
x = c(80,79,83,84,78,60,82,85,79,84,80,62) # factory (x)
y = c(300,302,315,330,300,250,300,340,315,330,310,240) # output
rel = lm(x~y)
rel
r = cor(x,y)
r

# Q 6
x = c(6,7,8,9,10) # no of sleeing hours
y = c(4,3,3,2,1) # no of hours watching TV
r = cor(x,y)
r
rel = lm(y~x)
k = data.frame(x=8)
predict(rel,k)

# Q 7
x = c(25,42,33,54,29,36) # test scores (x) 
y = c(42,72,50,90,45,48) # sales in the first month (y)
r = cor(x,y)
r
rel = lm(y~x)
k = data.frame(x=47)
predict(rel,k)
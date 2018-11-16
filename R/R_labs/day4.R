

# Day 4 - 29 OCT 2018

df = data.frame(sname = c("Anu","Mini","Leena"), rollno=c(123,234,45),marks=c(40,45,49))
df

df1 = data.frame(" "=c("Alex","Lilly","Mark"), Age = c(25,31,23), Height = c(177,163,190), Weight=c(57,69,83), Sex=c("F","F","M"))
df1
df2 = data.frame(" "=c("Alex","Lilly","Mark"),Working = c("Yes","No","No"))
df2
df3 = cbind(df1,df2[2])
df3 

class(df1[1])
class(df1[2])
class(df1[3])
class(df1[4])
mean(c(df1[3]))
a =c(df1[3])
a
class(a)
avg = mean(unlist(c(df1[3])))     
avg

unlist(c(df1[3]))/100
bmi = unlist(c(df1[4]))/(unlist(c(df[3]))/100)          
bmi
df3 = data.frame(BMI=c(bmi))
df3
df4 = cbind(df1,df3[1])
df4
df5 = cbind(df1,which(df4[4]>25))
df5            

list.files()
getwd()


fdata = read.table('/home/ai29/Desktop/common/R/Day4/Data/records1.txt')
fdata

csData = read.csv('/home/ai29/Desktop/common/R/Day4/Data/houses.csv')
csData

r = c("R1","R2")
c = c("C1","C2","C3")
m = c("Matrix1", "Matrix2","Matrix 3")
arr = array(1:30, dim =c(2,3,3), list(r,c,m))
arr

df5 = data.frame(mtcars$mpg, mtcars$cyl,mtcars$hp)
df5

mtcars[1:5,]
class(mtcars[6:11,])
head(mtcars,5)
head(mtcars,6:11)
length(mtcars)
?head
ncol(mtcars)

df7 = data.frame(mtcars[1:5,])
df7
df8 = data.frame(mtcars[6:11,])
df8
df9 = rbind(df7,df8)
df9

add = function(a, b =1) {
  x = a + b
  print(x)
}

div = function(a, b =1) {
  x = a / b
  return(x)
}
add(2,1)
add(b=10,a=20)
v = div(11,2)
v

ls()
getwd()
setwd('/home/ai19')
list()
setwd('/home/ai29')
list()

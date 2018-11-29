
# Question 1
demo(graphics)

# Question 2
x = sample(1:20,4, replace =TRUE)
lab = c("Comedy", "Action", "Romance", "Science/Fiction")
col1 = c("red","green","blue","purple")
pie(x,lab,col=col1, main='Movie Preferences', clockwise = TRUE)
legend("topleft",lab, fill = col1, cex=0.7)
box()

# Question 3
barplot(x,ylab="Preference",xlab="Movies", main="Movie Preferences",names.arg =lab, col=col1, border='blue')

# Question 5
products = c("A","B","C")
lab= c("Q1","Q2","Q3","Q4")
m = matrix(sample(1:20,12, replace=T), nrow=3,ncol=4)
m
barplot(m,xlab="Products", ylab="Sales", names.arg =lab, col=col1, broder='yellow')
legend("topleft",products, fill = col1, cex=0.7)

# Question 6
head(mtcars)
hist(mtcars$mpg)

# Question 7
plot.new()
plot.window()
plot.window(xlim=c(0,12),ylim=c(0,13))
axis(1)
axis(2)
abline(h=0)
abline(v=0)
#points(1:6,1:6)
px = c(2,4,6,8)
py = c(2,3,7,9)
points(px,py,"b")
abline(h=max(py))
abline(v=min(py))


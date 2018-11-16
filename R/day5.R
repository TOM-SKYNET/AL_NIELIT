

demo(graphics)

# Question 1
x = sample(1:20,4, replace =TRUE)
lab = c("Comedy", "Action", "Romance", "Science/Fiction")
col1 = c("red","green","blue","purple")
pie(x,lab,col=col1, main='Movie Preferences', clockwise = TRUE)
legend("topleft",lab, fill = col1, cex=0.9)
box()

# Question 2
barplot(x,ylab="Preference",xlab="Movies", main="Movie Preferences",names.arg =lab, col=col1, border='blue')

# Question 3
products = c("A","B","C")
m = matrix(sample(1:20,12, replace=T), nrow=4)
m
barplot(m,xlab="Products", ylab="Sales", names.arg =products, col=col1, broder='yellow')

# Question 4
head(mtcars)
hist(mtcars$mpg)

# Question 7
plot.new()
plot.window()
plot.window(xlim=c(0,10),ylim=c(0,10))
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

import numpy as np
import cv2 as cv
apple=cv.imread('./Questions/apple.jpg')
grc = cv.cvtColor(apple,cv.COLOR_BGR2GRAY)
grcN = cv.bitwise_not(grc)
print "grc:\n",grc
print "----------------------------------------"
print "grcN:\n",grcN
print "----------------------------------------"

print "np.subtract(grc,grcN).mean()", np.subtract(grc,grcN).mean()
if np.subtract(grc,grcN).mean():
    print "There is a differnce in Image"
else:
    print "No Difference in Image"


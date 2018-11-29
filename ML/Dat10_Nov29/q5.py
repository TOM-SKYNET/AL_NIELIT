import numpy as np
import cv2 as cv
apple=cv.imread('./Questions/apple.jpg')
grc = cv.cvtColor(apple,cv.COLOR_BGR2GRAY)
grcN = cv.bitwise_not(grc)
print "grc:",grc
print "grcN:",grcN
cv.imshow('Apple Gray',grcN)
cv.waitKey(0)




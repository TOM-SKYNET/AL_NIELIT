import numpy as np
import cv2 as cv
apple=cv.imread('./Questions/apple.jpg')
orange=cv.imread('./Questions/orange.jpg')
w,h = apple.shape[:2]
print 'Apple:', w,h
ow,oh = orange.shape[:2]
print 'Orange:', ow,oh
orange[:h,:w/2,:] = apple[:h,:w/2,:]
cv.imshow('Apple B Orange',orange)
cv.waitKey(0)

import numpy as np
import cv2 as cv
img=cv.imread('./Questions/apple.jpg')
rows,cols,_ = img.shape
m = cv.getRotationMatrix2D(((cols-1)/2,(rows-1)/2),45,1)
dst=cv.warpAffine(img,m,(rows,cols))
cv.imshow('Apple 45D Rotated',dst)
cv.waitKey(0)

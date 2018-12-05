import numpy as np
import cv2 as cv
img=cv.imread('./Questions/apple.jpg')
rows,cols,_=img.shape
M=np.float32([[1,0,200],[0,1,100]])
#dst=cv.warpAffine(img,M,(img.shape[0],img.shape[1]))
dst=cv.warpAffine(img,M,(rows,cols))
cv.imshow('Apple',dst)
cv.waitKey(0)

"""
	3) Do noise removal in the girl.jpg image using the above program (Q2).
"""
import cv2 as cv
import numpy as np

img = cv.imread('./Class/girl.jpg',0)
kernel = np.ones((2,2),np.uint8)
open1 = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
#cv.imshow('Erosin-Dilated Image',open1)
#cv.waitKey(0)

open2 = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
img_all = np.hstack((img,open1,open2))
cv.imshow('Erosin-Dilated Image',img_all)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img_all,'MORPH_CLOSE OPEN',(10,500), font, 4,(255,255,255),2)
cv.waitKey(0)

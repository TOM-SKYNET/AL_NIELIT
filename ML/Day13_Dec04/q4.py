"""
	4) Apply Sobel feature detection fuctions on the 'building.png' picture
"""
import cv2 as cv
import numpy as np

img = cv.imread('./Class/building.png')
a = img
for i in range(2):
    a = cv.pyrDown(a)
    
# X Order
sobelx = cv.Sobel(a, cv.CV_8U,1,0, ksize=1)
# Y order
sobely = cv.Sobel(a, cv.CV_8U,0,1, ksize=1)
# horizotal stacking
sobel_xy = np.hstack((a,sobelx,sobely))
cv.imshow('Sobel X  - Y Factor',sobel_xy)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(sobel_xy,'Sobel X - Y Factor',(10,500), font, 4,(255,255,255),2)
cv.waitKey(0)


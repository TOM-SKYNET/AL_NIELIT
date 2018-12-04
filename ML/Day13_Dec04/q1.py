import cv2 as cv
import numpy as np

img = cv.imread('./Class/j.png',0)
kernel = np.ones((2,2),np.uint8)
erosin = cv.erode(img,kernel,iterations=1)
cv.imshow('Eroded Imange',erosin)
cv.waitKey(0)

dialation = cv.dilate(img, kernel, iterations=1)
cv.imshow("Dilated Image",dialation)
cv.waitKey(0)

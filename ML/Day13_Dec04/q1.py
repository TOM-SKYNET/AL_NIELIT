"""
	1) Try to remove the noise from the man.jpg image by doing erosion and dilation in a sequence.
"""

import cv2 as cv
import numpy as np

img = cv.imread('./Class/man.jpg',0)
kernel = np.ones((2,2),np.uint8)
# Errosion
erosin = cv.erode(img,kernel,iterations=1)
cv.imshow('Eroded Imange',erosin)
cv.waitKey(0)

# Dilation
dialation = cv.dilate(img, kernel, iterations=1)
cv.imshow("Dilated Image",dialation)
cv.waitKey(0)

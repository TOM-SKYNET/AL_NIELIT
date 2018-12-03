
'''
    3) Apply adaptive thresholding to make the sudoku.jpg image more reader. Try
    to do the same with other similar images.
'''
import cv2 as cv
import numpy as np

img=cv.imread('../Day11_Nov30/Class/sudoku.jpg',0)

ret=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
print(ret)
cv.imshow('Adaptive Threshold',ret)
cv.waitKey(0)


'''
    1 . Write a program to apply various thresholding operations on the image
    gradient.jpg. Apply the same with other similar images and analyze the
    results.
        THRESH_BINARY
        THRESH_BINARY_INV
        THESH_TRUNC
        THRESH_TOZERO
        THRESH_TOZERO_INV

'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../Day11_Nov30/Class/gradient.jpg')
img1 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh1 = cv.threshold(img1,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img1,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img1,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img1,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img1,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

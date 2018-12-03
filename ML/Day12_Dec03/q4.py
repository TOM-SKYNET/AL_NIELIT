
'''
    4) Make the opencvlogo smoother by applying blur function. Try it with other
    images.
'''
import cv2 as cv
import numpy as np

img=cv.imread('../Day11_Nov30/Class/opencvlogo.png')
blur=cv.blur(img,(5,5))

cv.imshow('Blured Image',blur)
cv.waitKey(0)

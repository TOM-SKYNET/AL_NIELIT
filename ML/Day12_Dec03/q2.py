
'''
    2) Blend the images OpenCVLogo.png and ml.png using addWeighted function
    in a 0.7:0.3 ratio. Try the same with other images.
'''
import cv2 as cv
import numpy as np

img1=cv.imread('../Day11_Nov30/Class/ml.png')
img2=cv.imread('../Day11_Nov30/Class/opencv-logo.png')

#dt = cv.add(img1, img2)

dt = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow("Added Weightage of 0.7, 0.3",dt)
cv.waitKey(0)

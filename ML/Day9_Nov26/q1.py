'''
    Create a black image of 512X512 dimension and fill region 50X50 with
    green color.

'''

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img[50:100,50:100] = (0,255,0)
cv.imshow("Image", img)
k = cv.waitKey(0)

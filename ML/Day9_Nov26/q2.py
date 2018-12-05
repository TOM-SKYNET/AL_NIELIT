'''
Create a black image of 512X512 dimension.
    a. Add a line from the point (10,1) to (500,100)
    b. Draw a rectangle with corner points at (10,1) and (500,100)

'''

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[50:100,50:100] = (0,255,0)
cv.line(img, (10,1),(500,100), (0,255,0), 8)
cv.rectangle(img, (10,1),(500,100),(255,0,0),3)
cv.imshow("Image", img)
k = cv.waitKey(0)

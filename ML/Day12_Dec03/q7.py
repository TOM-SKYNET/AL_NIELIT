
'''
    7) Apply edge detection algorithm canny on the messi.jpg image.
'''
import cv2 as cv
import numpy as np

img = cv.imread("../Day11_Nov30/Class/messi.jpg",0)
edges1 = cv.Canny(img,100,200)
edges2 = cv.Canny(img,0,200)
img1 = np.hstack((img,edges1,edges2))
        
cv.imshow('Edge Detection',img1)
cv.waitKey(0)

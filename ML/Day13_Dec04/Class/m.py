import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Sunset.jpg')
b=cv.medianBlur(img)
cv.imshow(b)
cv.waitKey(0)

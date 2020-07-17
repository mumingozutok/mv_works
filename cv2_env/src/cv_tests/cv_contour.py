import cv2 as cv
import numpy as np

img = cv.imread('cv2_env/src/3_4.jpg',1)

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0,255,0), 1)

cv.imshow('frame',img)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
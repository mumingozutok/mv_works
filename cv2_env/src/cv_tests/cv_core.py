import cv2
import numpy as np

img = cv2.imread('cv2_env/src/0_1.jpg')

cv2.imshow('frame',img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
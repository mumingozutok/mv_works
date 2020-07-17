import cv2
import numpy as np

#create a black image
img = np.zeros((512,512,3),np.uint8)

#draw a blue diagonal with thickness 5
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img,(50,50),(100,100),(0,255,0),3)
img = cv2.circle(img,(200,200),100,(0,0,255),2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Hello OpenCV",(300,300),font,1,(255,255,255),1)

cv2.imshow('frame',img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
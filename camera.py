from asyncore import read 
import cv2
from matplotlib import image
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while(1):

    ret, frame = cap.read()
 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue1 = np.array([110,10,10])
    blue2 = np.array([130,255,255])
    mask = cv2.inRange(gray,blue1,blue2)

    cv2.imshow('frame',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 

cap.release()
cv2.destroyAllWindows()

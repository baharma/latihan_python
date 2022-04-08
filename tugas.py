import cv2
from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread("Megumin-2.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h , w = img.shape[:2]
cv2.imshow("hasil",img2)

dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)



brighness = 50 
cv2.imshow("sebelum di batasi", img2+brighness)
for i in np.arange(h):
    for j in np.arange(w):
        a = img2.item(i,j)
        if a>50:
            a=255
  
        else :
            a=0
        img2.itemset((i,j),a)

newheight, newwidth = h/4, w/4
T = np.float32([[1,0,newwidth], [0,1,newheight]])
img_translation = cv2.warpAffine(img2, T, (w, h))
image = cv2.rotate(img_translation, cv2.cv2.ROTATE_90_CLOCKWISE)


cv2.imshow('hasil',image)


waitKey(0)
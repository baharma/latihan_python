import cv2
import numpy as np

img = cv2.imread('Megumin-2.jpg',0)
row, colum = img.shape

img1 = np.zeros((row, colum), dtype='uint8')

min_range = 10
max_range = 100

for i in range(row):
    for j in range(colum):
        if img[i, j]>min_range and img[i, j]<max_range:
            img1[i, j] = 255
            
        else :
            img1[i, j] =0

cv2.imshow('slide image', img1)
cv2.waitKey(0)
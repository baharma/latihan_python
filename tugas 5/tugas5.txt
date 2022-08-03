import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('w1IkY.png',0)
img = cv2.medianBlur(img,5)

print(img.dtype)
img_neg = 255 - img
cv2.imshow('negatif',img_neg)
min_img = np.zeros((img.shape[0],img.shape[1]),dtype='uint8')

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        min_img[i,j] = 255*(img[i,j]-np.min(img))/(np.max(img)-np.min(img))

cv2.imshow('minmax',min_img)
img = cv2.imread("cicek.png",0)
img_rgb = cv2.imread("cicek.png")

h = img.shape[0]
w = img.shape[1]

img_thres= []
n_pix = 0
# loop over the image, pixel by pixel
for y in range(0, h):
    for x in range(0, w):
        # threshold the pixel
        pixel = img[y, x]
        if pixel < 0.5:
            n_pix = 0
        img_thres = n_pix[y, x]

cv2.imshow("cicek", img_thres)

cv2.waitKey(0)
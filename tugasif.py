import cv2
from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np


print('1 View Image Size')
print('2. Convert Image to Grayscale')
print('3. Convert Image to Biner')
print('4. Rotate Image ')
print('5. Geser Image')


pilihan = input('Pilihlah sesuai yg ada di atas  : ')
img = cv2.imread("Megumin-2.jpg")

h , w = img.shape[:2]
cv2.imshow("hasil",img)

if pilihan == '1':
    dimensions = img.shape
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)


elif pilihan == '2':
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', gray)

elif pilihan == '3':
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, bw_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary", bw_img)

if pilihan == '4':
    degree = 60
    rotasi= cv2.getRotationMatrix2D((w/2,h/2),degree,1)
    hasil = cv2.warpAffine(img,rotasi,(h,w))
    cv2.imshow('hasil',hasil)
elif pilihan == '5':
    M = np.float32([[1,0,100],[0,1,50]])
    dst = cv2.warpAffine(img,M,(w,h))

    cv2.imshow('img',dst)
else :
    print('gak milih')

waitKey(0)
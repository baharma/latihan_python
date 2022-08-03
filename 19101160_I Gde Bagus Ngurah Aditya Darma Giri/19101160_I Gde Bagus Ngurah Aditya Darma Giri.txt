from audioop import minmax
import cv2
from cv2 import waitKey
from cv2 import COLOR_BAYER_BG2BGR
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image


print('1 View Image Size')
print('2. Convert Image to Grayscale')
print('3. Convert Image to Biner')
print('4. Rotate Image ')
print('5. Geser Image')
print('6. Negatif Image')
print('7.Streching contras ')
print('8.Tresholding image ')


pilihan = input('Pilihlah sesuai yg ada di atas  : ')
img = cv2.imread("Megumin-2.jpg")
img2 = cv2.imread("Megumin-2.jpg",0)

h , w = img.shape[:2]
h1,w1 = img2.shape[:2]

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

elif pilihan == '6':
    img_neg = cv2.bitwise_not(img)
    cv2.imshow('img negative',img_neg)
    cv2.waitKey(0)
elif pilihan == '7':
    image = np.zeros((img2.shape[0], img2.shape[1]),dtype='uint8')

    min = np.min(img2)
    max = np.max(img2)

    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            image[i,j] =255*(img2[i,j] - min)/(max-min)
            cv2.waitKey(0)

elif pilihan == '8':
    imge = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(imge, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(imge, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(imge, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(imge, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(imge, 120, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('Binary Threshold', thresh1)
    cv2.imshow('Binary Threshold Inverted', thresh2)
    cv2.imshow('Truncated Threshold', thresh3)
    cv2.imshow('Set to 0', thresh4)
    cv2.imshow('Set to 0 Inverted', thresh5)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

else :
    print('gak milih')

waitKey(0)
import cv2
import numpy as np

img = cv2.imread('Megumin-2.jpg',0)

lst = [] 
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append(np.binary_repr(img[i][j],width=8))


eight_bit_img = (np.array([int(i[0])for i in lst] ))
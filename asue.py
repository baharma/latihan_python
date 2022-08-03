import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Untitled-3.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)

#filter
kernel = np.ones((5,5),np.float32)/25

kvl= cv2.filter2D(img, -1,kernel)

lp = cv2.blur(img,(5,5))

title = ['original', '2d Convulution', 'low pass']
image = [img,kvl,lp]

for i in range(3):
    plt.subplot(2,3,i+1), plt.imshow(image[i])
    plt.title(title[i])
    plt.xticks([]),plt.yticks([]),

    plt.show()
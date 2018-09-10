import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('out.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('img.jpg',gray)

#you need to set the thresholding parameters 
ret, thresh = cv2.threshold(gray,50,127,cv2.THRESH_BINARY)
cv2.imwrite('img1.jpg',thresh)

#you need to set the size of the kernel for closing
kernel = np.ones((50,50), np.uint8)
open1 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('color_img1.jpg', open1)
cv2.waitKey()
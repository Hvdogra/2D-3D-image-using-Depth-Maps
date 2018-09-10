import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('download.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('img.jpg',gray)
# ret, thresh = cv2.threshold(gray,50,127,cv2.THRESH_BINARY)
# cv2.imshow('img1',thresh)
ret1, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('image', thresh)
cv2.imwrite('color_img.jpg', thresh)
kernel = np.ones((15,15), np.uint8)
open1 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('color_img1.jpg', open1)

# open2 = cv2.morphologyEx(open1, cv2.MORPH_CLOSE, kernel)
# cv2.imshow('color_img2.jpg', open2)

final = thresh | open1
cv2.imwrite('color_img2.jpg', open1)
cv2.waitKey()
# 双边滤波
import cv2

img = cv2.imread('test3.jpg', 1)
cv2.imshow('src', img)

dst = cv2.bilateralFilter(img, 15, 35, 35)

cv2.imshow('dst', dst)
cv2.waitKey(0)

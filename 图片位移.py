import cv2
import numpy as np

img = cv2.imread('test.jpg', 0)

height, width = img.shape

matAffine = np.float32([[1, 0, 100], [0, 1, 100]])

affineImg = cv2.warpAffine(img, matAffine, (height, width))

cv2.imshow('origin image', img)
cv2.imshow('affine image', affineImg)

cv2.waitKey(0)

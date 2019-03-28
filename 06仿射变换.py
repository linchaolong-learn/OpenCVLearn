import cv2
import numpy as np

img = cv2.imread('test.jpg')

height, width, channel = img.shape

# 左上角 左下角 右上角，三点确定一个面
matSrc = np.float32([[0, 0], [height, 0], [0, width]])
# 目标点
matDst = np.float32([[30, 30], [height - 150, 150], [150, width - 150]])

# 获取仿射变换矩阵
matAffine = cv2.getAffineTransform(matSrc, matDst)

newImg = cv2.warpAffine(img, matAffine, (height, width))

cv2.imshow('original', img)
cv2.imshow('new image', newImg)

cv2.waitKey(0)

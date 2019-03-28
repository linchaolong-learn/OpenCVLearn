import cv2
import numpy as np


def resizeImg(img):
    """
    缩放图片
    """
    # 获取图片的宽高
    height, width, channels = img.shape

    # resized = cv2.resize(img, (int(width/2), int(height/2)))
    resized = cv2.resize(img, (int(width / 2), int(height / 2)), fx=.5, fy=.5)

    return resized


def resizeImgByAffine(img):
    """
    通过仿射变换缩放图片
    """

    # [[A1 A2 B1],[A3 A4 B2]]
    # [[A1 A2],[A3 A4]]  [[B1],[B2]]
    # newX = A1*x + A2*y+B1
    # newY = A3*x +A4*y+B2
    # x->x*0.5 y->y*0.5
    # newX = 0.5*x

    height, width, channel = img.shape

    matResize = np.float32([[0.5, 0, 0], [0, 0.5, 0]])

    resizedImg = cv2.warpAffine(img, matResize, (int(height/2), int(width/2)))

    return resizedImg


img = cv2.imread('test.jpg')

print(img.shape)

# resizedImg = resizeImg(img)
resizedImg = resizeImgByAffine(img)

cv2.imshow('original', img)

cv2.imshow('resized', resizedImg)

cv2.waitKey(0)

# 最近领域插值
# 双线性插值
# 像素关系重采样
# 立方插值

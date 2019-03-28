import cv2
import numpy as np

img = cv2.imread('test.jpg', 0)


def moveByAffine(img):
    """
    通过仿射变换函数实现位移
    """

    height, width = img.shape

    matAffine = np.float32([[1, 0, 100], [0, 1, 100]])

    return cv2.warpAffine(img, matAffine, (height, width))


def moveByMatrix(img):
    """
    自定义位移实现
    """
    height, width = img.shape

    newImg = np.zeros((height, width), np.uint8)

    for y in range(0, height - 100):

        for x in range(0, width - 100):
            newImg[y + 100, x + 100] = img[y, x]

    return newImg


def moveByMatrixOptimize(img):
    """
    自定义位移实现优化（通过矩阵截取实现）
    """
    height, width = img.shape

    newImg = np.zeros((height, width), np.uint8)

    newImg[100:, 100:] = img[:height - 100, : width - 100]

    return newImg


# affineImg = moveByAffine(img)
# affineImg = moveByMatrix(img)
affineImg = moveByMatrixOptimize(img)

cv2.imshow('origin image', img)
cv2.imshow('affine image', affineImg)

cv2.waitKey(0)

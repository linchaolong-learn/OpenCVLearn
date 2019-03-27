import cv2
import numpy as np


def flipImage(img):
    """
    图片镜像效果
    """
    height, width, channel = img.shape

    # 创建一个两倍height的矩阵
    newShape = (height * 2, width, channel)

    newImg = np.zeros(newShape, np.uint8)

    for y in range(0, height):

        for x in range(0, width):
            newImg[y, x] = img[y, x]

            newImg[newShape[0] - y - 1, x] = img[y, x]  # 行倒置

    newImg[height, :] = (0, 0, 255)  # 在中间画一条红线

    return newImg


def flipImageOptimize(img):
    """
    图片镜像效果优化
    """
    # flipud Flip an array vertically (axis=0).   垂直翻转
    # fliplr Flip an array horizontally (axis=1). 水平翻转
    return np.concatenate((img, np.flipud(img)))  # 将原图和一个垂直翻转后的图片合并


img = cv2.imread('test.jpg', 1)

# newImg = flipImage(img)
newImg = flipImageOptimize(img)

cv2.imshow('Flip Vertical', newImg)

cv2.waitKey(0)

import cv2
import numpy as np


def drawText():
    img = cv2.imread('test.jpg')

    # 使用opencv自带的字体
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.rectangle(img, (50, 50), (300, 150), (255, 0, 0))

    # 1 图片矩阵 2 文本 3 位置 4 字体 5 字体大小 6 颜色 7 线条厚度 8 线条类型
    cv2.putText(img, 'english', (100, 100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('img', img)

    cv2.waitKey(0)


def drawImage():
    """
    在图片中绘制图片

    其实就是直接覆盖原图的像素点
    """
    img = cv2.imread('test.jpg')

    imgResize = cv2.resize(img, (100, 100))

    img[100:200, 100:200] = imgResize

    cv2.imshow('img', img)

    cv2.waitKey(0)


# drawText()
drawImage()

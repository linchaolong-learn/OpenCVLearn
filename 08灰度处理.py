import cv2
import numpy as np


def gray1():
    """
    通过 imread 第二个参数读取灰度图片
    """
    img = cv2.imread('test.jpg', 0)  # flags 0 灰度图片 1 彩色图片

    cv2.imshow('gray image', img)

    cv2.waitKey(0)


def gray2():
    """
    通过 cvtColor 转换灰度图
    """
    img = cv2.imread('test.jpg')

    dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 颜色空间转换 1 data 2 BGR gray

    cv2.imshow('dst', dst)

    cv2.waitKey(0)


def gray3():
    """
    通过设置 RGB 均值实现灰度处理

    RGB R=G=B = gray  (R+G+B)/3
    """

    img = cv2.imread('test.jpg')

    height, width, channel = img.shape

    dst = np.zeros((height, width, channel), np.uint8)

    for y in range(0, height):

        for x in range(0, width):
            dst[y, x] = np.mean(img[y, x])

    cv2.imshow('dst', dst)

    cv2.waitKey(0)


def gray4():
    """
    gray = r*0.299+g*0.587+b*0.114
    """
    img = cv2.imread('test.jpg')

    height, width, channel = img.shape

    dst = np.zeros((height, width, channel), np.uint8)

    for y in range(0, height):

        for x in range(0, width):
            b, g, r = img[y, x]

            # gray = r * 0.299 + g * 0.587 + b * 0.114

            # 浮点 -> 定点
            # gray = (r * 1 + g * 2 + b * 1) / 4

            # +- */ >>
            gray = (r + (g << 1) + b) >> 2

            dst[y, x] = gray

    cv2.imshow('dst', dst)

    cv2.waitKey(0)


gray4()

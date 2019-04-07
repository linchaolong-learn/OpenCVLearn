import cv2
import numpy as np


def ImageHist(image, type):
    color = (255, 255, 255)
    windowName = 'Gray'
    if type == 31:
        color = (255, 0, 0)
        windowName = 'B Hist'
    elif type == 32:
        color = (0, 255, 0)
        windowName = 'G Hist'
    elif type == 33:
        color = (0, 0, 255)
        windowName = 'R Hist'

    # 完成直方图数据统计（注意这里参数一定要用中括号括起来）
    # 1 image 2 直方图的通道 3 mask 蒙版 不用到传None 4 直方图的size（柱子的数量） 5 统计的颜色值范围0-255
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])

    # 获取直方图最大最小值与其坐标
    minV, maxV, minL, maxL = cv2.minMaxLoc(hist)

    histImg = np.zeros([256, 256, 3], np.uint8)

    for h in range(256):
        intenNormal = int(hist[h] * 256 / maxV)  # 数据归一到0-256之间
        cv2.line(histImg, (h, 256), (h, 256 - intenNormal), color)  # 画线

    cv2.imshow(windowName, histImg)
    return histImg


img = cv2.imread('test.jpg', 1)

# 通道分离
channels = cv2.split(img)  # RGB - R G B

for i in range(0, 3):
    ImageHist(channels[i], 31 + i)  # 显示每个通道的直方图

cv2.waitKey(0)

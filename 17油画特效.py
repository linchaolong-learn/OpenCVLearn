# 1 gray 2 7*7 10*10 3 0-255 256 4 640-63 64-127
# 3 10 0-63 99
# 4 count 5 dst = result

import cv2
import numpy as np

img = cv2.imread('test.jpg', 1)
cv2.imshow('src', img)

imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 3), np.uint8)

for i in range(4, height - 4):
    for j in range(4, width - 4):

        # 将灰度分为8个等级，256(0-255)/8=32
        array1 = np.zeros(8, np.uint8)
        for m in range(-4, 4):
            for n in range(-4, 4):
                p1 = int(gray[i + m, j + n] / 32)  # 计算出每个点对应的等级
                array1[p1] = array1[p1] + 1  # 统计所有等级的数量

        # 找出最大的等级
        currentMax = array1[0]
        l = 0
        for k in range(0, 8):
            if currentMax < array1[k]:
                currentMax = array1[k]
                l = k

        # 简化 均值
        for m in range(-4, 4):
            for n in range(-4, 4):
                if gray[i + m, j + n] >= (l * 32) and gray[i + m, j + n] <= ((l + 1) * 32):
                    (b, g, r) = img[i + m, j + n]

        dst[i, j] = (b, g, r)

cv2.imshow('dst', dst)
cv2.waitKey(0)

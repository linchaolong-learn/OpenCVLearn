# 中值滤波 3*3
# 取中间值代替原来像素值的过程
# 比如，这里定义一个3*3的模板，然后进行排序，取其中的中间值代替原来的像素值
import cv2
import numpy as np

img = cv2.imread('test3.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('src', img)

dst = np.zeros((height, width, 3), np.uint8)
collect = np.zeros(9, np.uint8)

for i in range(1, height - 1):

    for j in range(1, width - 1):

        # 把3*3矩阵中像素添加到集合
        k = 0
        for m in range(-1, 2):
            for n in range(-1, 2):
                gray = img[i + m, j + n]
                collect[k] = gray
                k = k + 1

        # 对集合进行排序
        # 0 1 2 3 4 5 6 7 8
        #   1
        for k in range(0, 9):
            p1 = collect[k]
            for t in range(k + 1, 9):
                if p1 < collect[t]:
                    mid = collect[t]
                    collect[t] = p1
                    p1 = mid

        # 取中值作为目标值
        dst[i, j] = collect[4]

cv2.imshow('dst', dst)
cv2.waitKey(0)

# 中值滤波去噪点的效果并不是很好

# 本质：统计每个像素灰度 出现的概率 0-255 p
# 累计概率
# 1 0.2  0.2
# 2 0.3  0.5
# 3 0.1  0.6
# 256
# 100 0.5 255*0.5 = new

# 均衡化：使用累计概率*255计算出新颜色值替代原来的颜色值

import cv2
import numpy as np

img = cv2.imread('test.jpg', 1)

# 准备灰度图
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray)

# 完成直方图数据统计
count = np.zeros(256, np.float)
for i in range(0, height):
    for j in range(0, width):
        pixel = gray[i, j]
        index = int(pixel)
        count[index] = count[index] + 1
for i in range(0, 255):
    count[i] = count[i] / (height * width)

# 计算累计概率
sum1 = float(0)
for i in range(0, 256):
    sum1 = sum1 + count[i]  # 当前颜色等级累计前面颜色等级的概率，最后一个颜色等级概率为1
    count[i] = sum1
# print(count)

# 计算映射表
map1 = np.zeros(256, np.uint16)
for i in range(0, 256):
    # 计算新颜色值替代原来的颜色值
    map1[i] = np.uint16(count[i] * 255)  # 新颜色指 = 累计概率*255

# 映射
for i in range(0, height):
    for j in range(0, width):
        pixel = gray[i, j]
        gray[i, j] = map1[pixel]

cv2.imshow('dst', gray)
cv2.waitKey(0)

# 1 0-255 2 概率
# 本质：统计每个像素灰度 出现的概率 0-255 p
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

count = np.zeros(256, np.float)

for i in range(0, height):
    for j in range(0, width):
        pixel = gray[i, j]
        index = int(pixel)
        count[index] = count[index] + 1  # 统计每个颜色值的个数

for i in range(0, 255):
    count[i] = count[i] / (height * width)  # 计算该颜色值在图片中的占比

x = np.linspace(0, 255, 256)  # x轴，0-255 平分为256份
y = count  # y轴，每个颜色值的占比

plt.bar(x, y, 0.9, alpha=1, color='b')
plt.show()
cv2.waitKey(0)

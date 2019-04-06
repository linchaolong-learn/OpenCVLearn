import cv2
import numpy as np

newImageInfo = (500, 500, 3)

dst = np.zeros(newImageInfo, np.uint8)
# 绘制矩形：1 目标矩阵 2 左上角 3 右下角 4 颜色（bgr） 5 线段宽度，-1表示填充
cv2.rectangle(dst, (50, 100), (200, 300), (255, 0, 0), 5)

# 绘制圆形：1 目标矩阵 2 中心点 3 半径 4 颜色 5 线段宽度，-1表示填充
cv2.circle(dst, (250, 250), 50, (0, 255, 0), 2)

# 绘制椭圆：1 目标矩阵 2 中心点 3 轴 4 椭圆的偏置角度 5 圆弧的开始角度 6 圆弧的结束角度 7 颜色 8 线段宽度，-1表示填充
# cv2.ellipse(dst, (256, 256), (150, 100), 60, 0, 180, (255, 255, 0), -1)

points = np.array([[150, 50], [140, 140], [200, 170], [250, 250], [150, 50]], np.int32)
print(points.shape)

# 矩阵转置，用于绘制多边形
# points = points.reshape((-1, 1, 2))
# print(points.shape)
# print(points)

# 绘制多边形 1 目标矩阵 2 点坐标集合 3 是否闭合 4 颜色
cv2.polylines(dst, [points], True, (0, 255, 255))
cv2.imshow('dst', dst)
cv2.waitKey(0)

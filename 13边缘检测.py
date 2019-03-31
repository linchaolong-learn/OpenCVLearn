import cv2

img = cv2.imread('test.jpg')

# 1. 转换灰度图
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. 高斯滤波，去除噪点
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 0)  # 第二个参数模板大小

# 3. 使用canny方法实现边缘检测
dst1 = cv2.Canny(imgGray, 50, 50)  # 图片经过卷积运算后如果这个点大于这个门限就认为这是一个边缘点，否则就认为是非边缘点
dst2 = cv2.Canny(imgBlur, 50, 50)

cv2.imshow('dst no gaussian blur', dst1)
cv2.imshow('dst', dst2)

cv2.waitKey(0)


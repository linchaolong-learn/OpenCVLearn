import cv2

# 读取图片
img = cv2.imread('test.jpg')

# 显示图片，并指定窗口名称
cv2.imshow('test', img)

# 等待
cv2.waitKey(0)

print('hello opencv')


import cv2

img = cv2.imread('test.jpg')

print(img.shape)

# 获取图片的宽高
height, width, channels = img.shape

# resized = cv2.resize(img, (int(width/2), int(height/2)))
resized = cv2.resize(img, (int(width/2), int(height/2)), fx=.5, fy=.5)

cv2.imshow('resized', resized)

cv2.waitKey(0)





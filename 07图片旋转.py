import cv2

img = cv2.imread('test.jpg')
height, width, channel = img.shape

# 1. center 旋转的中心点 2.angle 旋转角度 3.scale 缩放倍数
matRotaion = cv2.getRotationMatrix2D((height*0.5, width*0.5), 45, 0.5)

rotationImg = cv2.warpAffine(img, matRotaion, (height, width))

cv2.imshow('original image', img)
cv2.imshow('roration image', rotationImg)

cv2.waitKey(0)

import cv2

img = cv2.imread('test.jpg')

print(img.shape)

height, width, channel = img.shape


cutImage = img[int(height/2):height, int(width/2): width]

cv2.imshow('origin image', img)

cv2.imshow('cut image', cutImage)

cv2.waitKey(0)

import cv2

img = cv2.imread('test.jpg')

# JPEG图片质量 0-100，数值越高质量越高，默认95
# https://docs.opencv.org/3.1.0/d4/da8/group__imgcodecs.html#ga292d81be8d76901bff7988d18d2b42ac
cv2.imwrite('test2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

# PNG图片压缩比 0-9，数值越高，图片越小
cv2.imwrite('test3.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])


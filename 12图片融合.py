# dst  = src1*a+src2*(1-a)
import cv2

img0 = cv2.imread('test.jpg', 1)
img1 = cv2.imread('test2.jpg', 1)

imgInfo = img0.shape
height = imgInfo[0]
width = imgInfo[1]

# ROI（截取图片合成部分）
roiH = int(height / 2)
roiW = int(width / 2)
img0ROI = img0[0:roiH, 0:roiW]
img1ROI = img1[0:roiH, 0:roiW]

# dst（合成图片）
dst = cv2.addWeighted(img0ROI, 0.5, img1ROI, 0.5, 0)  # add src1*a+src2*(1-a)

# 1 src1 2 a 3 src2 4 1-a
cv2.imshow('dst', dst)
cv2.waitKey(0)

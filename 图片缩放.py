import cv2


def resizeImg(img):
    """
    缩放图片
    """
    # 获取图片的宽高
    height, width, channels = img.shape

    # resized = cv2.resize(img, (int(width/2), int(height/2)))
    resized = cv2.resize(img, (int(width / 2), int(height / 2)), fx=.5, fy=.5)

    return resized


def resizeImgByAffine(img):
    """
    通过仿射变换缩放图片
    """
    return img


img = cv2.imread('test.jpg')

print(img.shape)

# resizedImg = resizeImg(img)
resizedImg = resizeImgByAffine(img)

cv2.imshow('resized', resizedImg)

cv2.waitKey(0)

# 最近领域插值
# 双线性插值
# 像素关系重采样
# 立方插值

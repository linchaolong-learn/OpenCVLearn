# p = p+40
# 原理：每个通道加上一个固定的常量实现亮度增强


def increaseLight():
    import cv2
    import numpy as np

    img = cv2.imread('test.jpg', 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    cv2.imshow('src', img)

    dst = np.zeros((height, width, 3), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            (b, g, r) = img[i, j]
            bb = int(b) + 40
            gg = int(g) + 40
            rr = int(r) + 40
            if bb > 255:
                bb = 255
            if gg > 255:
                gg = 255
            if rr > 255:
                rr = 255
            dst[i, j] = (bb, gg, rr)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)


def increaseLight2():
    """
    亮度加强的第二种方式，乘以一个系数在加上一个固定常量
    """
    # p = p+40
    # p = p*1。2+40
    # g+r P*piexl = new
    import cv2
    import numpy as np
    img = cv2.imread('test.jpg', 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    cv2.imshow('src', img)
    dst = np.zeros((height, width, 3), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            (b, g, r) = img[i, j]
            bb = int(b * 1.3) + 10
            gg = int(g * 1.2) + 15

            if bb > 255:
                bb = 255
            if gg > 255:
                gg = 255

            dst[i, j] = (bb, gg, r)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)


increaseLight2()

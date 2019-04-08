def gaussianFilter():
    """
    高斯均值滤波，能去除一些噪点，但图片也会变得模糊
    """
    import cv2
    img = cv2.imread('test3.jpg', 1)
    cv2.imshow('src', img)
    dst = cv2.GaussianBlur(img, (5, 5), 1.5)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)


def averageFilter():
    """
    均值滤波，使用均值代替原来像素值的过程
    """
    # 均值 6*6 1 。 * 【6*6】/36 = mean -》P
    import cv2
    import numpy as np
    img = cv2.imread('test3.jpg', 1)
    cv2.imshow('src', img)

    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    dst = np.zeros((height, width, 3), np.uint8)

    for i in range(3, height - 2):

        for j in range(3, width - 2):
            sum_b = int(0)
            sum_g = int(0)
            sum_r = int(0)

            # 6*6的矩阵，求矩阵每个通道颜色值的和
            for m in range(-3, 3):  # -3 -2 -1 0 1 2
                for n in range(-3, 3):
                    (b, g, r) = img[i + m, j + n]
                    sum_b = sum_b + int(b)
                    sum_g = sum_g + int(g)
                    sum_r = sum_r + int(r)

            # 求矩阵中每个通道颜色值的均值
            b = np.uint8(sum_b / 36)
            g = np.uint8(sum_g / 36)
            r = np.uint8(sum_r / 36)

            # 使用均值替代原图对应位置的像素
            dst[i, j] = (b, g, r)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)


# gaussianFilter()
averageFilter()

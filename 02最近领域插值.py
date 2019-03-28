import cv2
import numpy as np


def resize(path, heightFactor, widthFactor):
    """
    通过自己编码实现最近领域插值算法实现图片缩放功能
    :param path: 图片图片路径
    :param heightFactor: 高缩放倍数
    :param widthFactor: 宽缩放倍数
    :return:
    """
    img = cv2.imread(path)
    height, width, channel = img.shape

    # 计算目标宽高
    dstHeight = int(height * heightFactor)
    dstWidth = int(width * widthFactor)

    # 创建一个目标宽高并且数据类型为8bit的矩阵
    resizedImg = np.zeros((dstHeight, dstWidth, channel), np.uint8)  # 0-255

    for row in range(0, dstHeight):  # 行

        for column in range(0, dstWidth):  # 列

            # 通过最近领域算法计算每个坐标的对于原图的像素点
            i = int(row * (height * 1.0 / dstHeight))
            j = int(column * (width * 1.0 / dstWidth))

            resizedImg[row, column] = img[i, j]

    return resizedImg


def main():
    resizedImg = resize('test.jpg', 1.5, 1.5)
    cv2.imshow('resized img', resizedImg)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

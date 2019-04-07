def dirtyImage():
    """
    生成一张被破坏的图片
    """
    import cv2
    img = cv2.imread('test.jpg', 1)
    for i in range(200, 300):
        img[i, 200] = (255, 255, 255)
        img[i, 200 + 1] = (255, 255, 255)
        img[i, 200 - 1] = (255, 255, 255)
    for i in range(150, 250):
        img[250, i] = (255, 255, 255)
        img[250 + 1, i] = (255, 255, 255)
        img[250 - 1, i] = (255, 255, 255)
    cv2.imwrite('dirty_image.jpg', img)
    cv2.imshow('dirty image', img)
    cv2.waitKey(0)


def fixImage():
    # 1 坏图 2 array 3 inpaint
    import cv2
    import numpy as np

    img = cv2.imread('dirty_image.jpg', 1)
    cv2.imshow('dirty image', img)

    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]

    # 生成一个单通道的描述修补位置的蒙版
    paint = np.zeros((height, width, 1), np.uint8)
    for i in range(200, 300):
        paint[i, 200] = 255
        paint[i, 200 + 1] = 255
        paint[i, 200 - 1] = 255
    for i in range(150, 250):
        paint[250, i] = 255
        paint[250 + 1, i] = 255
        paint[250 - 1, i] = 255
    cv2.imshow('paint', paint)

    # 1 被破坏了的图片 2 标记了修补位置的蒙版 3 修补半径 4 修补方式
    imgDst = cv2.inpaint(img, paint, 3, cv2.INPAINT_TELEA)

    cv2.imshow('image', imgDst)
    cv2.waitKey(0)

# dirtyImage()
# fixImage()

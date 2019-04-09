import cv2

cap = cv2.VideoCapture('1.mp4')  # 获取一个视频文件的句柄
isOpened = cap.isOpened()  # 视频是否可以打开
print('isOpened=%s' % isOpened)

fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 宽
print('fps=%s, height=%s, width=%s' % (fps, height, width))

# 截取10张图片
count = 1
while cap.isOpened():
    if count > 10:
        break
    flag, frame = cap.read()
    if flag:  # 如果成功截取图片，保存到本地
        cv2.imwrite('capture%s.jpg' % count, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
    count += 1

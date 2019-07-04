# https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html
import cv2 as cv

# 1. 加载已经训练好的xml文件
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# 2. 读取图片
img = cv.imread('face2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('src', img)

# 3. 检测人脸
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print('face=', len(faces))

for (x, y, w, h) in faces:
    # 添加方框标识
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 人脸的灰度图，用作眼睛检测
    roi_gray = gray[y:y + h, x:x + w]
    # 人脸的原图，添加矩形标识
    roi_color = img[y:y + h, x:x + w]

    # 4. 检测眼睛
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print('eyes=', len(eyes))
    for (ex, ey, ew, eh) in eyes:
        # 添加方框标识
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv.imshow('dst', img)
cv.waitKey(0)
cv.destroyAllWindows()

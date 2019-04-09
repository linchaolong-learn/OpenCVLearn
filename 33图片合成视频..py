import cv2

img = cv2.imread('capture1.jpg')
imgInfo = img.shape
size = (imgInfo[1], imgInfo[0])
print(size)

# 1 文件名称 2 编码器（视频的存储要经过压缩编码的，而不是一帧一帧直接存储），-1自动选择一个支持的编码器 3. 帧率 4. 视频的宽高
videoWrite = cv2.VideoWriter('merge.mp4', -1, 5, size)  # 写视频

for i in range(1, 11):
    fileName = 'capture' + str(i) + '.jpg'
    img = cv2.imread(fileName)
    videoWrite.write(img)  # 写入方法 1 jpg data

print('end!')

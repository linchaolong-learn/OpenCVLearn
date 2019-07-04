# svm本质 寻求一个最优的超平面 分类
# svm 核：line
# 身高体重 训练 预测
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 准备数据
rand1 = np.array([[155, 48], [159, 50], [164, 53], [168, 56], [172, 60]])
rand2 = np.array([[152, 53], [156, 55], [160, 56], [172, 64], [176, 65]])

# 2. 标签
label = np.array([[0], [0], [0], [0], [0], [1], [1], [1], [1], [1]])

# 3. 数据
data = np.vstack((rand1, rand2))
data = np.array(data, dtype='float32')

# svm 所有的数据都要有label
# [155, 48] -- 0 女生，[152,53] -- 1 男生
# 监督学习


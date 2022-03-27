# 4.已知矩阵[[-1,1,0],[-4,3,0],[1,0,2]]，求矩阵的特征向量、特征值、矩阵的逆。
# import numpy as np
# A=np.array([[-1,1,0],[-4,3,0],[1,0,2]])
# print("原矩阵：\n",A)
# e,v=np.linalg.eig(A)
# print("矩阵特征值与特征向量 e v:\n",e,v,sep='\n')
# print("矩阵的逆：\n",np.linalg.inv(A))
# print("特征向量的乘积：\n",np.dot(A,v))
# print("特征值与特征向量的乘积：\n",e*v)
# print("验证二者是否相等：\n",np.isclose(np.dot(A,v),e*v))
# print("det函数：\n",np.linalg.det(A-np.eye(3,3)*e))

# 5.
# x1=np.array([1,5,6,3,-1])
# x2=np.arange(12).reshape(3,4)
# 利用Numpy求向量和矩阵的1，2范数，并说明其含义。
# import numpy as np
# x1=np.array([1,5,6,3,-1])
# x2=np.arange(12).reshape(3,4)
# print("x1:\n",x1)
# print("x2:\n",x2)
# print("向量x1 1范数:",np.linalg.norm(x1))
# print("向量x1 2范数:",np.linalg.norm(x1,ord=2))
# print("向量x2 1范数:",np.linalg.norm(x2))
# print("向量x2 2范数:",np.linalg.norm(x2,ord=2))


# 6. (简答题)
# 6.求解矩阵np.matrix([[1,2,3], [4,5,6], [7,8,9]])的奇异值分解结果。

# import numpy as np
# a=np.matrix([[1,2,3], [4,5,6], [7,8,9]])
# print("矩阵a:",a)
# u,s,v=np.linalg.svd(a)
# print(f'奇异值分解:\n'
#       f'u:\n{u}\n'
#       f's:\n{s}\n'
#       f'v:\n{v}\n')
# print(f'验证：\n{u*np.diag(s)*v}')


# 7.应用题，运行并理解下面程序，将运行结果截图上传。
# SVD用于图像压缩
# 我们有多少次遇到过这个问题？我们喜欢用我们的智能手机浏览图像，并随机将照片保存。然后突然有一天 ，提示手机没有空间了！而图像压缩有助于解决这一问题。
# 它将图像的大小(以字节为单位)最小化到可接受的质量水平。这意味着你可以在相同磁盘空间中存储更多图像。
# 图片压缩利用了在SVD之后仅获得的一些奇异值很大的原理。你可以根据前几个奇异值修剪三个矩阵，并获得原始图像的压缩近似值，人眼无法区分一些压缩图像。以下是在Python中编写的代码：
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import cv2
#
# # 灰度化读取图片
# img = cv2.imread('PDSU.jpg', 0)
#
# # 得到svd
# U, S, V = np.linalg.svd(img)
#
# # 得到矩阵的形状
# print(U.shape, S.shape, V.shape)
#
# # 以不同component数绘制图像
# comps = [638, 500, 400, 300, 200, 100]
#
# plt.figure(figsize=(16, 8))
# for i in range(6):
#     low_rank = U[:, :comps[i]] @ np.diag(S[:comps[i]]) @ V[:comps[i], :]
#     if (i == 0):
#         plt.subplot(2, 3, i + 1), plt.imshow(low_rank, cmap='gray'), plt.axis('off'), plt.title(
#             "Original Image with n_components =" + str(comps[i]))
#     else:
#         plt.subplot(2, 3, i + 1), plt.imshow(low_rank, cmap='gray'), plt.axis('off'), plt.title(
#             "n_components =" + str(comps[i]))
# plt.savefig('svd.jpg')
# plt.show()

# # 3. 利用Numpy产生正态分布图，理解下面代码，并给每行代码进行注释
import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
sampleNo = 1000
# 一维正态分布, 下面三种方式是等效的
mu = 3
sigma = 0.1
np.random.seed(0)             # 使得随机数据可预测。
s = np.random.normal(mu, sigma, sampleNo)  # 从正态（高斯）分布中抽取随机样本。
plt.subplot(141)              # 表示把显示界面分割成1*4的网格。其中，第一个参数是行数，第二个参数是列数，第三个参数表示图形的标号。
plt.hist(s, 30, normed=True)  # 绘制直方图  这个参数是指定每个bin(箱子)分布的数据,对应x轴  这个参数指定bin(箱子)的个数,也就是总共有几条条状图

np.random.seed(0)
s = sigma * np.random.randn(sampleNo) + mu
plt.subplot(142)
plt.hist(s, 30, normed=True)
np.random.seed(0)
s = sigma * np.random.standard_normal(sampleNo) + mu
plt.subplot(143)
plt.hist(s, 30, normed=True)

# 二维正态分布
mu = np.array([[1, 5]])
Sigma = np.array([[1, 0.5], [1.5, 3]])
R = cholesky(Sigma)  #
s = np.dot(np.random.randn(sampleNo, 2), R) + mu
plt.subplot(144)
# 注意绘制的是散点图，而不是直方图
plt.plot(s[:,0],s[:,1],'+')
plt.show()


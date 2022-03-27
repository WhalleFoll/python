#1
# import numpy as np
# x=np.array((1,2,3))
# y=np.array((4,5,6))
# print(np.dot(x,y))
# print(x.dot(y))
# print(sum(x*y))
#
# x=np.matrix([[1,2,3],[4,5,6]])
# y=np.matrix([1,2,3,4,5,6])
# print(x,y,x[1,1],sep='\n\n')
#

# 2
# import  numpy as np
# import random
# data_zero=np.zeros((2,3))
# data_one =np.ones((3,4))
# data_random=np.random.randint(0,10,(3,2))
# print(data_zero)
# print(data_one)
# print(data_random)

# #t2
# 1）a=np.array([[1,2,3],[4,5,6]])（查看数组的维度，数组元素的个数）。
# 2）将a数组的行变列，返回最后一个元素，返回第2到第4个元素，返回逆序的数组
# 3）a=np.arange(9).reshape(3,3)
# b=np.arange(9).reshape(3,3)
# 将a、b数组水平合并，垂直合并，深度合并
# 4）将a数组水平拆分，垂直拆分，深度拆分
# 5）数组运算（与常的四则运算，与数组的四则运算，判断数组是否相等）
# a=np.arange(4,dtype=np.float32).reshape(2,2)
# b=np.arange(4,8,dtype=np.float32).reshape(2,2)
# 求a+2,a+b,a/b,a*b,判断数组a,b是否相等
# 6）对数组a求和、积、平均值、最大值、最小值、元素替换、方差、标准差
# print(f'税前薪资是：{salary}元， 缴税：{tax}元， 税后薪资是：{aftertax}元')
import  numpy as np

a=np.array([[1,2,3],[4,5,6]])

print(f'维度：{a.shape} 元素个数：{a.size}')
a_trans = a.transpose()
print(f'行列交换：{a_trans} ')

a=np.arange(9).reshape(3,3)
b=np.arange(9).reshape(3,3)
print(f'a b垂直合并：\n{np.vstack((a, b))}\n'
      f'a b水平合并：\n{np.hstack((a, b))}\n'
      f'a b深度合并：\n{np.dstack((a,b))}\n')
print('-----------------------------------')



a=np.arange(4,dtype=np.float32).reshape(2,2)
b=np.arange(4,8,dtype=np.float32).reshape(2,2)

print(f'a+2:\n{a+2}\n'
      f'a+b:\n{np.add(a,b)}\n'
      f'a*b:\n{np.multiply(a,b)}\n'
      f'a/b:\n{np.divide(a,b)}\n')



#4.已知矩阵[[-1,1,0],[-4,3,0],[1,0,2]]，求矩阵的特征向量、特征值、矩阵的逆。
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


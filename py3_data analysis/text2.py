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

#
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
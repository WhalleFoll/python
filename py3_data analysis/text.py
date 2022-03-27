# from functools import reduce
# from operator import add ,mul ,or_
#

#
# seg=range(1,10)
# print(reduce(add,seg))
# print(reduce(mul,seg))
# seg=[{1},{2},{3},{4}]
# print(reduce(or_,seg))

# triangle = [[1],[1,1]]
# for i in range(2,9):
#     neline=[]
#     neline.append(1)
#     for j in range(i-1):
#         value = triangle[i-1][j]+triangle[i-1][j+1]
#         neline.append(value)
#     neline.append(1)
#     triangle.append(neline)
# print(triangle)


#
# L=[[1],[1, 1]]
# def triangles(L,cen):
#     n=3
#     while n <= cen:
#         for i in range(0,n-1):
#             L.append([])
#             if i==0:
#                 L[n-1].append(1)
#                 L[n-1].append(1)
#             else:
#                 L[n-1].insert(i,L[n - 2][i]+L[n - 2][i - 1])
#         n=n+1
#     return 'done'
#
# triangles(L,8)
# #遍历
# for i in range(8):
#     print(L[i])


# import random
# import string
#
# a = string.ascii_letters + string.digits
# key = []
#
# def getKey():   #
#     key = random.sample(a, 8)
#     return "".join(key)
#
# for i in range(5):  #遍历
#     print(getKey())


# from functools import reduce
# from operator import add ,mul ,or_
#
# seg=range(1,10)
# print(reduce(add,seg))
# print(reduce(mul,seg))
# seg=[{1},{2},{3},{4}]
# print(reduce(or_,seg))

# def check_id_length(n):  # 判断身份证号长度是否正确
#     if len(str(n)) != 18:
#         return False
#     else:
#         return True
# def check_id_data(n):  # 检查数据
#     factor = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
#     last = ("1", "O", "X", "9", "8", "7", "6", "5", "4", "3", "2")
#     n = str(n)
#     sum = 0
#     if int(n[16]) % 2 == 0:  # 判断第17位是否为偶数
#         gender = "女"
#     else:
#         gender = "男"
#     for i in range(0, 17):
#         sum += int(n[i]) * factor[i]  # 求前17位与加权数相乘的和
#     sum %= 11  # 取余，计算余数对应的第18位身份证号
#     if (last[sum]) == str(n[17]):  # 第18位相同
#         print("身份证号规则校验通过，校验码是:"+str(last[sum])+"，该身份证号使用者为"+str(gender)+"性")
#         return sum
#     else:
#         print("当前身份证号校验失败，校验码应为:"+str(last[sum])+"，当前校验码是:"+str(n[17]))
#         return 0
# n = input("请输入18位身份证号:")
# if check_id_length(n):
#     check_id_data(n)
# else:
#     print("身份证号位数不正确,请重新输入!")

# id_card=input('请输入身份证号码：')
#
# jy = id_card[len(id_card)-1:len(id_card)]  # 截取校验位
# if len(id_card) == 18:  # 判断输入的身份证号是否为18位
#     x= (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
#     s=0
#     for i in range(1,len(id_card)): # 遍历身份证号
#         e = id_card[i-1:i]
#         s = s + int(e)*x[i-1]       # 求前17位与加权数相乘的和411
#     b = s%11
#     y=("1","O","X","9","8","7","6","5","4","3","2")
#     c = y[b]
#     if jy == c:   # 判断校验位是否相同
#         print('经计算校验码为',c,'和实际相同,身份证合法！')
#     else:
#         print('经计算校验码为',c,'和实际不同，身份证不合法！')


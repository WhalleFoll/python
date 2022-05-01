#7.1
# from copy import deepcopy
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# arr =np.array([0,1,2])
# missing_data=pd.read_csv('./7/missing_data.csv',names=arr)
# print("lagrange插值前\n",missing_data.notnull())
#
# #拉格朗日插值
# from scipy.interpolate import lagrange
# for i in range(0,3):
#     la = lagrange(missing_data.loc[:,i].dropna().index,missing_data.loc[:,i].dropna().values)
#     list_d=list(set(np.arange(0,21)).difference(set(missing_data.loc[:,i].dropna().index)))
#     missing_data.loc[list_d,i]=la(list_d)
#     print("第%d列缺失值的个数%d"%(i,missing_data.loc[:,i].isnull().sum()))
# print("",missing_data.notnull())
# print(missing_data)


# 7.2
# import pandas as pd
# ele_loss =pd.read_csv('./data_7/ele_loss.csv',encoding='utf-8')
# alarm =pd.read_csv('./data_7/alarm.csv',encoding='utf-8')
# #查看两个表的形状
# print('ele_loss:',ele_loss.shape)
# print('alarm',alarm.shape)
#
# #合并数据
# merge = pd.merge(ele_loss,alarm,left_on=["ID","date"],right_on=["ID","date"],how="inner")
# print("合并后表的形状：",merge.shape)
# print("合并后表:",merge)

#7.3
# import pandas as pd
# import numpy as np
#
# a=pd.read_csv('./data_7/model.csv',encoding='utf-8')
# def sjcl(d):
#     d=(d-d.mean())/d.std()
#     return d
# m=sjcl(a)
# m.head

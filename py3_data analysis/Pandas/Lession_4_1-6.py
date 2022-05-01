# 1
# import  pandas as pd
# import  matplotlib.pyplot as plt
#
# pd.set_option('display.unicode.ambiguous_as_wide',True)
# pd.set_option('display.unicode.east_asian_width',True)
#
# s1 =pd.Series(range(1,20,5))
#
# s2 =pd.Series({'语文':90,'数学':92,'Python':98,'物理':87,'化学':92})
#
# s1[3] = -17
# s2['语文']= 94
# print('s1 原始数据'.ljust(20,'='))
# print(s1)
#
# print('对 s1求绝对值'.ljust(20,'='))
# print(abs(s1))
#
# print('s1所有值+5'.ljust(20,'='))
# print(s1+5)
#
# print('s1 每行索引 +2'.ljust(20,'='))
# print(s1.add_prefix(2))
#
# print('s2原始数字：'.ljust(20,'='))
# print(s2)
#
# print('s2数字直方图'.ljust(20,'='))
# s2.hist()
# plt.show()
#
# print('s2的每行索引后面+张三'.ljust(20,'='))
# print(s1.add_suffix('_张三'))
#
# print('s2最大索引'.ljust(20,'='))
# print(s2.idxmax())
#
# print('测试s2的值是否是否在指定区间内'.ljust(20,'='))
# print(s2.between(90,94,inclusive=True))
#
# print('查看s2 90分以上的'.ljust(20,'='))
# print(s2[s2>90])
#
# print('查看s2大于中值数据'.ljust(20,'='))
# print(s2[s2>s2.median()])
#
# print('s2与数字之间的运算'.ljust(20,'='))
# print(round(s2**0.5)*10,1)
#
# print('S2a的中值'.ljust(20,'='))
# print(s2.median())
#
# print('s2 中最小的2个值'.ljust(20,'='))
# print(s2.nsmallest(2))
#
# print('两个Series对象相加')
# print(pd.Series(range(5))+pd.Series(range(5,10)))
#
# print('每个值的平方对5的余数')
# print(pd.Series(range(5)).pipe(lambda  x,y,z:(x**y)%z,2,5))
#
# print('每个值加3 后乘以3'.ljust(20,'='))
# print(pd.Series(range(5)).pipe(lambda x:x+3).pipe(lambda x:x*3))
#
# print('每个值加3'.ljust(20,'='))
# print(pd.Series(range(5)).apply(lambda x:x+3))
#
# print('标准差 ,无偏方差，无偏标准差'.ljust(20,'='))
# print(pd.Series(range(5)).std())
# print(pd.Series(range(5)).var())
# print(pd.Series(range(5)).sem())
#
# print('查看是否存在等价与TRUE的值'.ljust(20,'='))
# print(any(pd.Series([3,0,True])))
#
# print('查看是否所有值是否等价与True'.ljust(20,'='))
# print(all(pd.Series([3,0,True])))


# 4.
# 练习验证下列代码，并对关键代码进行注释
# （1）课件中的案例1
# 项目背景
# 集团这几年孵化了50个品牌，在各渠道做了大量品宣层面的曝光。现在集团首席官提了两个需求：
# 要一张大表，包含每个月搜索人数TOP5的品牌相关数据，以及对应品牌在当月的搜索份额和排名。

# 导入相关包
# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 查看19年1月份的样例数据
# df = pd.read_excel('data/品牌投放/2019-01.xlsx')   # 读取data/品牌投放 文件加下的 2019-01.xlsx 文件
# print(df.info())      # 打印简要摘要
# print(df.head())      # head( )函数的原型中，默认的参数size大小是 5，所以会返回 5 个数据。
# # 按搜索人数排名
# df = df.sort_values('品牌搜索人数', ascending=False)   #数据进行排序，该函数即可根据指定列数据也可根据指定行的数据排序。 是否按指定列的数组升序排列，默认为True，即升序排列
#
# df['搜索人数排名'] = df['品牌搜索人数'].rank(ascending=False)  #排名   # 加上排名列
# df.head()
# df['搜索份额'] = df['品牌搜索人数'] / df['品牌搜索人数'].sum()  # 计算搜索份额指标
# df.head()            # head( )函数的原型中，默认的参数size大小是 5，所以会返回 5 个数据。
#
# data_list = []      #空列表
#
# #遍历 data/品牌投放 所有文件
# # 生成data_list 表 以及对应品牌在当月的搜索份额和排名(前五)
# for name in os.listdir('data/品牌投放/'):
#     df = pd.read_excel(f'data/品牌投放/{name}')
#     df = df.sort_values('品牌搜索人数', ascending=False)       #排序（降序）
#     df['搜索人数排名'] = df['品牌搜索人数'].rank(ascending=False)
#     df['搜索份额'] = df['品牌搜索人数'] / df['品牌搜索人数'].sum()
#
#     brand = '凌云'
#     brand_data = df.loc[df['品牌'].str.find(brand) != -1, :]
#
#     other = df.loc[df['品牌'].str.find(brand) == -1, :]
#     other_top5 = other.iloc[:5, :]
#     data = pd.concat([brand_data, other_top5])
#     data['日期'] = name[:-5]
#     #    print(data)
#
#     data_list.append(data)  #数据插入
#
# result = pd.concat(data_list)   #拼接，   解决两个表或者多个表按照纵向或者横向拼接。
# print(result.head(20))          #打印头部 8行



# 5  课件中的案例2
# 目前能够拿到的，只有品牌、搜索人数、点击人数和对应支付人数这几个指标。
# 要找到最近一年投放效果还不错的品牌，我们可以用漏斗思维，从量级（人数）和效率（转化率）两个角度来考虑：
# 在费用无差别的情况下：
# 人群基数大（搜索人数），表示投放的心智效果不错，让更多用户被广告触达后，在平台主动搜相关的品牌。
# 搜索-点击转化率高，代表了搜索结果的精准度，搜索后展示页面的吸引力等等
# 点击-支付转化率高，更可能受产品详情页面、活动力度等影响
# 导入相关包
# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 筛选出2020年订单
# data_list = []
# for name in os.listdir('data/品牌投放/'):
#     df = pd.read_excel(f'data/品牌投放/{name}')
#     df['日期'] = name[:-5]
#     data_list.append(df)
#
# final = pd.concat(data_list)
# final_last = final.loc[final['日期'].str.find('2020') != -1, :]
#
# print('数据行数：{}'.format(len(final_last)))
# final_last.head()
# # 提取关键字段，按品牌分组
# gp = final_last.groupby('品牌')[['品牌搜索人数', '点击人数', '支付人数']].sum().reset_index()
# gp = gp.sort_values('品牌搜索人数', ascending=False)
# gp.head()
# # 计算关键字段
# gp['搜索-点击转化率'] = gp['点击人数'] / gp['品牌搜索人数']
# gp['点击-支付转化率'] = gp['支付人数'] / gp['点击人数']
# gp.head()
# # 设置字体避免中文乱码
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# # TOP15搜索品牌图形绘制
# draw_data = gp.iloc[:15, :]
#
# my_dpi = 80
# plt.figure(figsize=(800 / my_dpi, 480 / my_dpi), dpi=my_dpi * 5)
#
# x = draw_data['搜索-点击转化率'].to_list()
# y = draw_data['点击-支付转化率'].to_list()
# z = draw_data['品牌搜索人数']
# text = draw_data['品牌'].to_list()
# plt.scatter(x, y, s=z / 1000, c=x, cmap="Reds", alpha=0.7, edgecolors="grey", linewidth=1)
#
# # enumerate()是python的内置函数
# # enumerate在字典上是枚举、列举的意思
# # 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
# # enumerate多用于在for循环中得到计数
# for i, txt in enumerate(text):
#     plt.text(x=x[i], y=y[i], s=txt, size=11, horizontalalignment='center', verticalalignment='center')
#
# plt.xlabel("搜索-点击转化率")  #设置x轴的标签
# plt.ylabel("点击-支付转化率")  #设置y轴的标签
# plt.title("TOP15品牌搜索分布")  #设置标题
# plt.show()



# 第六题
# 任务2 pandas数据分析基础（完成以下操作）2学时
# 5. 使用pandas读取Excel、CSV、JSON文件，并将三个文件内容合并到一个表，写入到EXCEL文件中；
# 6. 读取“student.xlsx”数据并实现以下操作
#
# （1）查看student文件中的表的个数，及表名，”学生综合完成情况”表数据集的元素的个数、维度、大小等信息，输出表的列名。
# （2）使用describe方法对整个”学生综合完成情况”表数据集进行描述性统计。
# （3）从”作业成绩”表中提取学生的作业成绩，得出每个学生作业的平均成绩，写入到作“业成绩表”中。
# （4）利用pandas读取student.xlsx-student6.xlsx文件中的“学生综合完成情况，作业成绩，成绩详情”表中的“学号、姓名、班级，视频观看时长，讨论数，章节学习次数，作业平均成绩，综合成绩，成绩等级，合并到一个表中。
# （5）计算不同班级，作业成绩和综合成绩的平均值。

# import pandas as pd
# # 列对齐
# pd.set_option('display.unicode.ambiguous_as_wide',True)
# pd.set_option('display.unicode.east_asian_width',True)
# df_excel = pd.read_excel(r'./data/read_excel.xlsx')
# df_csv =pd.read_csv(r'./data/read_csv.csv',encoding='gb2312')
# df_json =pd.read_json(r'./data/read_json.json')
# print(len(df_excel),len(df_json),len(df_csv))
# df_all = pd.concat([df_excel,df_csv,df_json],ignore_index=True)
# print(df_all)
# df_all.to_excel('./mer_e_c_s.xlsx')

#6 (1)
# import pandas as pd
# # 列对齐
# pd.set_option('display.unicode.ambiguous_as_wide',True)
# pd.set_option('display.unicode.east_asian_width',True)
# df=pd.read_excel('./data/student.xlsx',sheet_name=None)
# print('表的个数',len(df.keys()),'\n各表名：',df.keys())
# df=pd.read_excel('./data/student.xlsx',sheet_name='学生综合完成情况')
# print('学生综合完成情况的元素个数：\n',df.size)
# print('学生综合完成情况的元素为数:\n',df.ndim)
# print('学生综合完成情况的元素大小：\n',df.shape)
# print('学生综合完成情况的表的列名：\n',df.columns)
# df.describe()
# df = pd.read_excel('./data/student.xlsx',sheet_name='作业成绩')
# df['平均成绩1']=df[['一','二','三','四','五']].mean(axis=1)
# print('学生综合完成情况的表的列名：\n',df)

#6 (4)

# import pandas as pd
# # 列对齐
# pd.set_option('display.unicode.ambiguous_as_wide',True)
# pd.set_option('display.unicode.east_asian_width',True)
# df=pd.read_excel('./data/student.xlsx',sheet_name='学生综合完成情况')
# dff=df[['学生姓名','学号/工号','班级','视频观看时长','讨论数','章节学习次数']]
# print(dff)
# df=pd.read_excel('./data/student.xlsx',sheet_name='作业成绩')
# dff2=df[['学生姓名','平均成绩']]
# print(dff2)
# df=pd.read_excel('./data/student.xlsx',sheet_name='成绩详情')
# dff3 =df[['学生姓名','学号/工号','班级','综合成绩','成绩等级']]
# print(dff3)
# df_all = pd.concat([dff,dff2,dff3],axis=1)
# print(df_all)

# 6 （5）
import pandas as pd
# 列对齐
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
datalist =[]
for i in range(7):
    if i==0:
        tablename = './data/student.xlsx'
    else:
        tablename ='./data/student'+str(i)+'.xlsx'

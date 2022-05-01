# 任务4
# 数据分析与可视化综合实验
# 2
# 学时
# 8.
# 数据分析与可视化
# （1）运行下面的程序，在当前文件夹中生成饭店营业额模拟数据文件data.csv。
import csv
import random
import datetime

fn = 'data.csv'

with open(fn, 'w') as fp:
    # 创建csv文件写入对象
    wr = csv.writer(fp, lineterminator='\n')
    # 写入表头
    wr.writerow(['日期', '销量'])

    # 生成模拟数据
    startDate = datetime.date(2017, 1, 1)

    # 生成365个模拟数据，可以根据需要进行调整
    for i in range(365):
        # 生成一个模拟数据，写入csv文件
        amount = 300 + i * 5 + random.randrange(100)
        wr.writerow([str(startDate), amount])
        # 下一天
        startDate = startDate + datetime.timedelta(days=1)


# （2）然后完成下面的任务：
# 1）使用pandas读取文件data.csv中的数据，创建DataFrame对象，并删除其中所有缺失值；
# 2）使用matplotlib生成折线图，反应该饭店每天的营业额情况，并把图形保存为本地文件first.jpg；
# 3）按月份进行统计，使用matplotlib绘制柱状图显示每个月份的营业额，并把图形保存为本地文件second.jpg；
# 4）按月份进行统计，找出相邻两个月最大涨幅，并把涨幅最大的月份写入文件maxMonth.txt；
# 5）按季度统计该饭店2017年的营业额数据，使用matplotlib生成饼状图显示2017年4个季度的营业额分布情况，并把图形保存

# 8.2.1
# from copy import deepcopy
# import pandas as pd
# import matplotlib.pyplot as plt
#
# pd.set_option('display.unicode.ambiguous_as_wide',True)
# pd.set_option('display.unicode.east_asian_width',True)
#
# df = pd.read_csv(r'./data.csv',encoding='gb2312')
#
# print('行数：',len(df))
# df = df.dropna()
# print(df)
# print('删除其中缺失值后的行数:',len(df))

# 8.2.2

# import matplotlib
# import pandas as pd
# import matplotlib.pyplot as plt
#
# matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
#
# df = pd.read_csv('data.csv', encoding='GBK')
# # 生成营业额折线图
# plt.figure()
# df.plot(x='日期')
# plt.savefig('first.jpg')


# 8.(2).3)
# import matplotlib
# import pandas as pd
# import matplotlib.pyplot as plt
#
# matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
#
# df = pd.read_csv('data.csv', encoding='GBK')
# # 按月统计，生成并保存柱状图
# plt.figure()
# df1 = df[:]
# df1['month'] = df1['日期'].map(lambda x: x[:x.rindex('-')])
# df1 = df1.groupby(by='month', as_index=False).sum()
# df1.plot(x='month', kind='bar')
# plt.savefig('second.jpg')

# 8.(2).4)

# import matplotlib
# import pandas as pd
# import matplotlib.pyplot as plt
#
# matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
#
# df = pd.read_csv('data.csv', encoding='GBK')
# # 查找涨幅最大的月份，写入文件
# df2 = df1.drop('month', axis=1).diff()
# m = df2['销量'].nlargest(1).keys()[0]
# with open('maxMonth.txt', 'w') as fp:
#     fp.write(df1.loc[m, 'month'])

# 8.(2).5)
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['KaiTi']

df1 = pd.read_csv('data.csv', encoding='GBK')
# 按季度统计，生成并保存饼状图
plt.figure()
one = df1[:3]['销量'].sum()
two = df1[3:6]['销量'].sum()
three = df1[6:9]['销量'].sum()
four = df1[9:12]['销量'].sum()
plt.pie([one, two, three, four],
        labels=['one', 'two', 'three', 'four'])
plt.savefig('third.jpg')
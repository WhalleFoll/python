
import csv
import random
import datetime

fn = 'cjdata.csv'
with open(fn, 'w', newline='') as fp:
    #创建csv文件写入对象
    wr = csv.writer(fp)
    #写入表头
    wr.writerow(['姓名','性别','高数','英语','Python'])

    for i in range(50):
        first_name = ["张", "曾", "李", "王", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "欧阳"]
        second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷",
                       "文", "明浩", "光", "超", "军", "达"]
        sex = ['男','女']
        name = random.choice(first_name) + ''.join(random.choice(second_name))
        gender = random.choice(sex)
        math = random.randint(30,100)
        english = random.randint(30, 100)
        Python = random.randint(30, 100)
        wr.writerow([name,gender,math,english,Python])
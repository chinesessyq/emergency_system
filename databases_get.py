import pymysql
import pandas as pd


# from select_username import *
# from select_data import *


def databases_get():
    data_change()
    data = data_select()
    dic = data_deal(data)
    return dic


# 连接数据库
def databases_connect():
    # 建立连接
    conn = pymysql.connect(
        user='root',  # 用户名
        password='mysql',  # 密码：这里一定要注意123456是字符串形式
        host='localhost',  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
        database='hello_world',  # 数据库的名字
        port=3306,  # 指定端口号，范围在0-65535
        charset='utf8mb4',  # 数据库的编码方式
    )
    return conn


# 更改数据库内数据
def data_change(sql_change='update stu set sage=17,sname="huahua" where sno=2;'):
    conn = databases_connect()
    cur = conn.cursor()
    cur.execute(sql_change)
    conn.commit()
    conn.close()
    cur.close()


# 查找数据
def data_select(sql_select='select * from stu;'):
    # 一般只要需要指定两个主要的参数sql和con，sql是sql查询语句，con指定上面建立的连接
    data = pd.read_sql(sql_select, con=databases_connect())
    # 关闭连接
    databases_connect().close()
    return data


# 不成熟的数据处理方式
def data_deal(data):
    # 处理数据
    list1 = []
    list2 = []
    lists = []
    # 将 DataFrame转化为array转化为list
    for i in data.values:
        # print(i)
        for j in i:
            list1.append(j)
    # print('list1', list1)
    # 拆分数据
    for index in range(len(list1)):
        # print(index)
        list2.append(list1[index])
        if len(list2) == 3:
            lists.append(list2)
            list2 = []
    dic = {}
    key = ['sno', 'sname', 'sage']
    i = 0
    # for j in range(len(lists) - 1):
    for value in key:
        dic[value] = str(lists[0][i])
        i += 1
    return dic

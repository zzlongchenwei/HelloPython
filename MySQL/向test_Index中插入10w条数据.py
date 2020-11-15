#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:向test_Index中插入10w条数据.py
@time:2020/11/15
"""
from pymysql import connect


def main():
    # 创建connection连接
    conn = connect(host='localhost', port=3306, database='python_test', user='root', password='weiwenhuamingZZ1',
                   charset='utf8')

    # 获得cursor对象
    cursor = conn.cursor()

    # 插入10w条数据
    for i in range(100000):
        cursor.execute("insert into test_index values('haha-%d')" % i)

    # 提交数据
    conn.commit()


if __name__ == '__main__':
    main()
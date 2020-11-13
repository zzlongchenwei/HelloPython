#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:查询一行数据.py
@time:2020/11/13
"""
from pymysql import *


def main():

    # 1.建立连接
    conn = connect(host='localhost', port=3306, user='root', password='weiwenhuamingZZ1', database='python_test',
                   charset='utf8')     # 必须所有参数本地都有，不然不会成功
    # 2.获取游标对象
    cursor = conn.cursor()  # 游标
    # 3.执行SQL语句
    students_table = cursor.execute("select * from students;")  # 执行SQL语句
    print(students_table)
    student_data = cursor.fetchone()
    print(student_data)
    student_data = cursor.fetchmany(3)
    print(student_data)
    # 4.关闭游标
    cursor.close()  # 关闭游标
    # 5.关闭连接
    conn.close()    # 关闭连接

if __name__ == '__main__':
    main()
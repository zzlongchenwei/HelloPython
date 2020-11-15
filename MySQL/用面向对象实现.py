#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:用面向对象实现.py
@time:2020/11/13
"""
from pymysql import connect


class ST:
    def __init__(self):
        # 创建连接
        self.conn = connect(host='localhost', port=3306, user='root', password='weiwenhuamingZZ1',
                            database='python_test',
                            charset='utf8')  # 必须所有参数本地都有，不然不会成功
        # 获得游标对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭游标对象
        self.cursor.close()
        # 关闭连接
        self.conn.close()

    def execute_sql(self, sql):
        """执行sql语句"""
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_datas(self):
        """显示所有学生列表"""
        sql = "select * from students;"
        self.execute_sql(sql)

    def show_height(self):
        """显示身高"""
        sql = "select name,height from students"
        self.execute_sql(sql)

    def show_age(self):
        """显示年龄"""
        sql = "select name,age from students"
        self.execute_sql(sql)

    def add_studet_data(self):
        """增加学生信息"""
        stu_name = input("学生姓名：")
        stu_age = input("学生年龄：")
        stu_height = input("学生身高：")
        stu_gender = input("学生性别（男1，女2，中性3，保密4）：")
        stu_class = input("学生班级：")
        sql = "insert into students values (0, '{:s}', {:d}, {:.2f}, {:d}, {:d},0) ;".format(
            stu_name, int(stu_age), float(stu_height), int(stu_gender), int(stu_class))
        self.cursor.execute(sql)  # 执行sql语句
        self.conn.commit()  # 提交后生效

    def get_info_by_name(self):
        """根据名字查询学生信息"""
        # 不安全方式，' or 1=1 or '1
        find_name = input("请输入要查询学生的名字：")
        # sql = "select * from students where name='{:s}'".format(find_name)
        # print("---->%s<----" % sql)
        # self.execute_sql(sql)

        # 安全方式
        sql = "select * from students where name=%s"
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall())

    @staticmethod
    def print_menu():
        print("----学生信息----")
        print("1: 所有学生信息")
        print("2: 所有学生身高")
        print("3: 所有学生年龄")
        print("4: 添加一个学生信息")
        print("5: 根据名字查学生信息")
        return input("请输入功能对应的序号:")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":  # 查询所有学生
                self.show_all_datas()
            elif num == "2":  # 查询学生身高
                self.show_height()
            elif num == "3":  # 查询学生年龄
                self.show_age()
            elif num == "4":  # 增加学生信息
                self.add_studet_data()
            elif num == "5":  # 根据名字查学生
                self.get_info_by_name()
            else:
                print("输入有误，重新输入...")


if __name__ == '__main__':
    students = ST()
    students.run()

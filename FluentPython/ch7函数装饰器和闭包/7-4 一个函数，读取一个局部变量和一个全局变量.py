# -*- coding: utf-8 -*-

# @File    : 7-4 一个函数，读取一个局部变量和一个全局变量.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-
b = 6


def f1(a):
    global b
    print(a)
    print(b)
    b = 9


f1(3)

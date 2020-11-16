#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:04-无参数、无返回值的函数的装饰.py
@time:2020/11/16
"""
def set_func(func):
    def call_func():
        print("---这是权限验证1----")
        print("---这是权限验证2---")
        func()

    return call_func


# 装饰器
@set_func   # 等价于test1 = set_func(test1)
def test1():
    print("---test1---")


# ret = set_func(test1)
# ret()

# test1 = set_func(test1)  # test1重新指向set_func(test1)
test1()  # 此时调用test1() 即 call_func()
print('==='*10)
test1()
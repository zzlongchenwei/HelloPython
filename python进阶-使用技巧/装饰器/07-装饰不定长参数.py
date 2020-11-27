#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:07-装饰不定长参数.py
@time:2020/11/21
"""


def set_func(func):
    print('开始装饰')

    # *相当于对元组拆包, **对字典拆
    def call_func(*args, **kwargs):  # 这也要有参数
        print("---这是权限验证1----")
        print("---这是权限验证2---")
        # func(args, kwargs) 相当于传递了两个参数，一个元组，一个字典
        func(*args, **kwargs)  # 这个即时原来函数

    return call_func


# 装饰器
@set_func  # 等价于test1 = set_func(test1)
# *args将多余参数，以元组保存
def test1(num, *args, **kwargs):  # 有参数
    print("---test1---%d" % num)
    print("---test1---", args)
    print("---test1---", kwargs)


test1(100)
print('*' * 20)
test1(100, 200)
print('*' * 20)
test1(100, 200, 300, mm=100)

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:09-多个装饰器对同一个函数装.py
@time:2020/11/21
"""


def permission(func):
    print('开始进行装饰权限1的功能')

    # *相当于对元组拆包, **对字典拆
    def call_func(*args, **kwargs):  # 这也要有参数
        print("---这是权限验证1----")
        # func(args, kwargs) 相当于传递了两个参数，一个元组，一个字典
        # 返回无人接收，所以返回None
        # func(*args, **kwargs)  # 这个即时原来函数
        return func(*args, **kwargs)

    return call_func


def set_func(func):
    print('开始装饰xxx的功能')

    # *相当于对元组拆包, **对字典拆
    def call_func(*args, **kwargs):  # 这也要有参数
        print("---这是xxx功能----")
        return func(*args, **kwargs)

    return call_func


@permission  # 后装   test1 = permission(set_func(test1))
@set_func  # 先装 test1 = set_func(test1)
def test1():  # 有参数
    print("---test1---")


test1()

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:01-装饰器演示.py
@time:2020/11/16
"""


def set_func(func):
    def call_func():
        print("---这是权限验证1----")
        print("---这是权限验证2---")
        func()

    return call_func


def test1():
    print("---test1---")


ret = set_func(test1)
ret()
print('==='*10)
test1()

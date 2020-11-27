#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:10-应用、多个装饰器对同一个函数装饰.py
@time:2020/11/21
"""


def set_func_1(func):
    def call_func():
        # '<h1>haha</h1>'
        # return func()
        return "<h1>" + func() + "</h1>"

    return call_func


def set_func_2(func):
    def call_func():
        return "<td>" + func() + "</td>"

    return call_func

@set_func_1 # 后装
@set_func_2 # 先装
def get_str():
    return "haha"


print(get_str())

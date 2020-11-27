#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:11-类装饰器.py
@time:2020/11/21
"""


# def set_func_1(func):
#     def call_func():
#         # '<h1>haha</h1>'
#         # return func()
#         return "<h1>" + func() + "</h1>"
#
#     return call_func


class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这是装饰器添加的功能")
        return self.func()



@Test  # 相当于get_str = Test(get_str)
def get_str():
    return "haha"


print(get_str())

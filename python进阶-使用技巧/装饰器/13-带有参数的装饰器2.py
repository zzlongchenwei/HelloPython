#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:13-带有参数的装饰器2.py
@time:2020/11/21
"""


def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print('---权限级别1，验证---')
            elif level_num == 2:
                print('---权限级别2，验证---')
            return func()

        return call_func

    return set_func


@set_level(1)
def test1():
    print("---test1---")
    return 'ok'


@set_level(2)
def test2():
    print("---test2---")
    return 'ok'


test1()
test2()

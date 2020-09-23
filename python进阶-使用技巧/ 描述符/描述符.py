#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:10717
@file:描述符.py
@time:2020/09/22
"""


# 代码 2

class Desc(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print("__get__...")
        print('name = ', self.name)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc('x')

    def __init__(self):
        self.y = Desc('y')


# 以下为测试代码
t = TestDesc()
t.x
t.y                 # y不会被打印

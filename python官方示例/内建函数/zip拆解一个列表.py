#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:zip拆解一个列表.py
@time:2020/10/29
"""

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
x2, y2 = zip(*zip(x, y))        # 与*运算符结合
print(list(zip(*zip(x, y))))    # 当只有一个 可迭代对象 参数时，它将返回一个单元组的迭代器。
print(x2)
print(y2)
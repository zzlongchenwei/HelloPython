#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:06-通过一个装饰器对多个函数进行装饰.py
@time:2020/11/21
"""
def set_func(func):
    def call_func(a):   # 这也要有参数
        print("---这是权限验证1----")
        print("---这是权限验证2---")
        func(a)  # 这个即时原来函数

    return call_func


# 装饰器
@set_func   # 等价于test1 = set_func(test1)
def test1(num):  # 有参数
    print("---test1---%d" % num)

@set_func
def test2(num):
    print("----test2----%d" % num)

test1(100)  # 此时调用test1() 即 call_func()
test2(200)  # 此时调用test1() 即 call_func()
print('==='*10)

"""
装饰器在执行之前就已经被调用了
"""
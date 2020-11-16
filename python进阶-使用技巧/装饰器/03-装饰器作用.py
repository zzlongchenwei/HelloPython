#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:03-装饰器作用.py
@time:2020/11/16
"""
import time


def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        stop_time =  time.time()
        print('all time is  %f' % (stop_time-start_time))

    return call_func


# 装饰器
@set_func   # 等价于test1 = set_func(test1)
def test1():
    print("---test1---")
    for i in range(100000):
        pass


# ret = set_func(test1)
# ret()

# test1 = set_func(test1)  # test1重新指向set_func(test1)
test1()  # 此时调用test1() 即 call_func()
print('==='*10)
test1()
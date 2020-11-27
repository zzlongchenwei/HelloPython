#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:12-带有参数的装饰器.py
@time:2020/11/21
"""
def set_func(func):
    def call_func(*args,**kwargs):
        level =args[0]
        if level==1:
            print('---权限级别1，验证---')
        elif level ==2:
            print('---权限级别2，验证---')
        return func()

    return call_func

@set_func
def test1():
    print("---test1---")
    return 'ok'



@set_func
def test2():
    print("---test2---")
    return 'ok'

test1(1)
test2(2)
# 这样做并不好，如果test1被调用次数多，都要修改传入参数
# 其次，test1() test2()中并没有参数，这样传本来要给calL_func()传参数，结果传给了test1() test2()
# test1()和test2()自己可以修改传入参数的，即自己可以改验证级别
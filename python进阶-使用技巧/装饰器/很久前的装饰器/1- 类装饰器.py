#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26

class Test(object):
    # 定义call后可以直接调
    def __call__(self):
        print("---test---")

t = Test()

t()

# __new__  __init__  __del__  __str__  __call__

class Test2(object):
    def __init__(self,func):
        print("---初始化---")
        print("func name is %s"%func.__name__)
        self.__func = func   # 让私有属性指向函数名
    def __call__(self):
        print("---装饰器中的功能---")
        self.__func()


def test():
    print("---test---")

@Test2      # 添加装饰器的时候就已经装了
            # test = Test(test)
def test():
    print("---test---")

test()      # 会调用Test的call

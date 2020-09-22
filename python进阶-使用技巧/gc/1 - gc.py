#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26

# 引用计数的缺点，没法解决循环引用，引用计数一直为1

class ClassA():
    def __init__(self):
        print('object born , id:%s '%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2

# python以引用计数为主，标记-清除和分代收集两种机制为辅的策略
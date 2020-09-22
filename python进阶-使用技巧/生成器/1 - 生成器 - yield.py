#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26

# 生成器
def creatNum():                 # 调用函数不会执行
    print("---start---")
    a,b = 0,1
    for i in range(5):
        print("---1---")
        yield b                 # yield会让函数在这停止，并且返回b的值，使用next()可以继续进行
        print("---2---")
        a,b = b,a+b
        print("---3---")
    print("---stop---")
# 创建了一个生成器对象
a = creatNum()

ret = next(a)           # 如果没执行过，将从creatNum()头开始执行，到yield停止
                        # 如果执行过了，就从停止的地方开始执行
# 注意：
# next(a)
# a.__next__()
# 以上两种方式等价
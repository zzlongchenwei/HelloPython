#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26


# 类也是一个对象，
# 类可以被动态创建
class Person(object):
    num = 0
    print("---person---test----")

    def __init__(self):
        self.name = "abc"

print(100)
print("hello")
print("tt")

print(Person)

# type()可以创建对象
Test2 = type("Test2", (), {})
# 最原始的创建类的哥们叫元类


# ------------------------------------
def printNum(self):
    print("---num-%d---"%self.num)

Test3 = type("Test3",() ,{"printNum":printNum})

t1 = Test3()
t1.num = 100
t1.printNum()
# -------------------------------------
class printNum2():
    def printNum(self):
        print("---num-%d---"%self.num)

# 这俩等价
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26

def test1():
    while True:
        print("---1---")
        yield None

def test2():
    while True:
        print("---2---")
        yield None

t1 = test1()
t2 = test2()
while True:
    t1.__next__()
    t2.__next__()

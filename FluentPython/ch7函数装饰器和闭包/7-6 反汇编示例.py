# -*- coding: utf-8 -*-

# @File    : 7-6 反汇编示例.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-
from dis import dis

b = 6


def f1(a):
    global b
    print(a)
    print(b)

dis(f1)

print('-'*20)
def f2(a):
    print(a)
    print(b)
    b = 9

dis(f2)
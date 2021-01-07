# -*- coding: utf-8 -*-

# @File    : 7-1装饰器通常通常吧把函数替换成另一个函数.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-
def deco(func):
    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running targert()')


target()
print(target)

# -*- coding: utf-8 -*-

# @File    : 7-23 为了接受参数，新的register装饰器必须作为函数调用.py
# @Date    : 2021-01-07
# @Author  : chenwei    -剑衣沉沉晚霞归，酒杖津津神仙来-
registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'
              % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decorate # 返回装饰器


@register(active=False)
def f1():
    print('running f1()')


@register() # 即使不传入参数，register也必须作为函数调用，即要返回真正的装饰器decorate
def f2():
    print('running f2()')


def f3():
    print('running f3()')

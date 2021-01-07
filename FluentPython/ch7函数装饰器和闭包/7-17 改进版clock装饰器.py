# -*- coding: utf-8 -*-

# @File    : 7-17 改进版clock装饰器.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-
import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(','.join(repr(arg) for arg in args))  # repr()将对象转化为供解释器读取的形式
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(','.join(pairs))
        arg_str = ','.join(arg_list)
        # arg_str = arg_list
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def f1(a, c, b=2):
    print(a, b, c)
    return a + b


f1(1, 2, b=3)

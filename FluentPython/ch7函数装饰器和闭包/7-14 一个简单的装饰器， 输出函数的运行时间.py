# -*- coding: utf-8 -*-

# @File    : 7-14 一个简单的装饰器， 输出函数的运行时间.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock  # snooze = clock(snooze)
def snooze(seconds):
    time.sleep(seconds)


@clock  # factorial = clock(factorial)
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! = ', factorial(6))
    print('*' * 40)
    print(factorial.__name__)   # clocked
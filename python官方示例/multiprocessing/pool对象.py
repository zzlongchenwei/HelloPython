#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:pool对象.py
@time:2020/10/28
"""

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))  # Pool赋予函数并行化处理输入值的能力，可以将输入值分配给不同的进程处理
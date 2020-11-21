#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:futures.as_completed()按任意顺序运行结果.py
@time:2020/11/21
"""
import random
import time
from concurrent import futures

def task(n):
    time.sleep(random.random())
    return (n, n / 10)

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: 开始')
wait_for = [
    ex.submit(task, i) for i in range(5, 0, -1)
]
for f in futures.as_completed(wait_for):
    print('main: result:{}'.format(f.result()))
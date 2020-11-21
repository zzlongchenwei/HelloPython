#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:futures执行单个任务.py
@time:2020/11/21
"""
from concurrent import futures
import threading
import time

def task(n):
    print('{}: 睡眠 {}'.format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print('{}: 执行完成 {}'.format(threading.current_thread().name, n))
    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main :开始')
f = ex.submit(task, 5)
print('main: future: {}'.format(f))
print('等待运行结果')
results = f.result()
print('main: result:{}'.format(results))
print('main: future 之后的结果:{}'.format(f))

"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12.1启动与停止线程.py
"""

# Code to execute in an independent thread
import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create and launch a thread
from threading import Thread

t = Thread(target=countdown, args=(10,))
t.start()

# 可以查询一个线程是否还在运行
if t.is_alive():
    print('still running')
else:
    print('Completed')

# Python 解释器直到所有线程都终止前仍保持运行
t.join()


# 对于需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程
t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
# 台线程无法等待，不过，这些线程会在主线程终止时自动销毁

"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12.2信号量实现上一个代码.py
"""
import threading


# Worker thread
def worker(n, sema):
    # Wait to be signaled
    sema.acquire()

    # Do some work
    print('Working', n)


# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

# 运行上边的代码将会启动一个线程池，但是并没有什么事情发生。这是因为所有的线程都在等待获取信号量。
# 每次信号量被释放，只有一个线程会被唤醒并执行，

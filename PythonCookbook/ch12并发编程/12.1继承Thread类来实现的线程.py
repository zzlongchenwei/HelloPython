"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12.1继承Thread类来实现的线程.py
"""

from threading import Thread
import time





class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


# c = CountdownThread(5)
# c.start()
import multiprocessing

c = CountdownThread(5)
# 可以通过 multiprocessing 模块在一个单独的进程中执行你的代码
p = multiprocessing.Process(target=c.run)
p.start()

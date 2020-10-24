"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12.1把线程放入一个类中.py
"""
import time
from threading import Thread
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n >0:
            print('T-minus', n )
            n -= 1
            time.sleep(1)


c = CountdownTask() # 实例化
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate() # signal termination
t.join()    # wait for actual termination (if needed)


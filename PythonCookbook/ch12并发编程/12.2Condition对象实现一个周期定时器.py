"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12.2Condition对象实现一个周期定时器.py
"""

import threading
import time


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)   # 一个定时器线程，运行重写的run
        t.daemon = True # 守护线程，背后执行不影响前面的线程

        t.start()

    def run(self):
        """
        Run the timer and notify waiting threads after each interval
        """
        while True:     # 定时器线程
            time.sleep(self._interval)  # 暂停
            with self._cv:      # 使用 with 语句会在它包围的代码块内获取关联的锁。
                self._flag ^= 1     # 将flag异或1
                self._cv.notify_all()   # 唤醒所有正在等待这个条件的线程

    def wait_for_tick(self):
        """
        Wait for the next tick of the timer
        """
        with self._cv:      # 使用 with 语句会在它包围的代码块内获取关联的锁。
            last_flag = self._flag  # self._flag=0 ,last_flag=0
            while last_flag == self._flag:  # last_flag == self._flag判定为True
                self._cv.wait()             # 就阻塞所在线程，直到调用了notify_all()唤醒_cv


# Example use of the timer
ptimer = PeriodicTimer(1)
ptimer.start()


# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n )
        n += 1


threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()

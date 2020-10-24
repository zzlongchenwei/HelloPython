"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/16  @author:zzlong  
@file:mtsleepB.py
"""

import _thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()  # 释放锁


def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()  # thread.allocate_lock()函数得到锁对象
        lock.acquire()  # acquire()方法取得（每个锁）。取得锁效果相当于“把锁锁上”
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i])) # 把后面元组传给前面的函数

    for i in nloops:
        while locks[i].locked(): pass   # 如果获取了锁对象则返回 True，否则，返回 False
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()







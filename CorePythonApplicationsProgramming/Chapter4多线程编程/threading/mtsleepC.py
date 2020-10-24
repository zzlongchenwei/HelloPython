"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/23  @author:zzlong  
@file:mtsleepC.py
"""

import threading
from time import sleep, ctime

loops = [1, 2]


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('string at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))   # 创建Thread实例
        threads.append(t)

    for i in nloops:    # start threads
        threads[i].start()  # 使用start()方法开始线程活动。

    for i in nloops:    # wait for all 这会阻塞调用这个方法的线程，直到被调用join()的线程终结
        threads[i].join()   # thread to finish
        # 主线程会被阻塞，其他两个子线程会继续运行。
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:进程池.py
@time:2020/11/01
"""
from multiprocessing import Pool
import os, time, random

def work(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))

    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop-t_start))


if __name__ == '__main__':
    po = Pool(3)
    for i in range(0, 10):
        po.apply_async(work, (i,))

    print("---start---")
    po.close()
    po.join()
    print("---end---")


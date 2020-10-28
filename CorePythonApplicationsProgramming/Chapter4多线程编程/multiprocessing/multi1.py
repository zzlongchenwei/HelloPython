"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/28  @author:zzlong  
@file:multi1.py
"""

import os
from multiprocessing import Process, Lock
import time

def whoami(label, lock):
    msg = '%s: name:%s, pid:%s'
    with lock:
        print(msg % (label, __name__, os.getpid()))     # 获得进程id


if __name__ == '__main__':
    lock = Lock()
    whoami('function call', lock)   # __name__ = __main__

    p = Process(target=whoami, args=('spawned child', lock))    # __name__ = __mp_main__
    p.start()
    # p.join()  # 等待spawned child进程结束

    for i in range(5):
        Process(target=whoami, args=(('run process %s' % i), lock)).start()

    with lock:
        print('Main process exit.')

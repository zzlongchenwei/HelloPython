"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/25  @author:zzlong  
@file:12.3get()pu()非阻塞和设定超时.py
"""

import queue


q = queue.Queue()
try:
    data = q.get(block=False)
except queue.Empty:    # Empty异常
    ...

try:
    data = q.put(item, block=False)
except queue.Full:    # Full异常
    ...

try:
    data = q.get(timeout=0.5)
except queue.Empty:    # Empty异常
    ...


def producer(q):
    ...
    try:
        q.put(item, block=False)    # 当队列满的时候就执行其他代码
    except queue.Full:      # 比如输出一条日志信息并丢弃
        log.warning('queued item %r discarded!', item)
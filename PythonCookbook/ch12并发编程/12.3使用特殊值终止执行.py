"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12.3使用特殊值终止执行.py
"""

from queue import Queue
from threading import Thread

# Object that signals shutdown
_sentinel = object()
# A thread that produces data
def producer(out_q):
    while running:  # 当producer没有正常运行的时候，队列读到_sentinel时就应该停止
        # Produce some data
        # ...
        out_q.put(data)
    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)     # 消费者在读到这个特殊值之后立即又把它放回到队列中，将之传递下去。
                                    # 这样，所有监听这个队列的消费者线程就可以全部关闭了
            break
        # Process the data
        ...
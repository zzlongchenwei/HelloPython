"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/25  @author:zzlong  
@file:12.3Event对象来监测处理的过程.py
"""

from queue import Queue
from threading import Thread, Event

# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
        ...
        # Make an (data, event) pair and hand it to the consumer
        evt = Event()
        out_q.put((data, evt))
        ...
        # Wait for the consumer to process the item
        evt.wait()

        # A thread that consumes data
        def consumer(in_q):
            while True:
                # Get some data
                data, evt = in_q.get()
                # Process the data
                ...
                # Indicate completion
                evt.set()
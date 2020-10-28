"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/25  @author:zzlong  
@file:阻塞模式导致数据污染.py
"""

import queue

q = queue.Queue(10)

for i in range(10):
    myData = 'A'
    q.put(myData)
    myData = 'B'

for i in range(10):
    ch = q.get()
    print(ch)

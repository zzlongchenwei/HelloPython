"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/25  @author:zzlong  
@file:等待对象任务被完成示例.py
"""

import threading, queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()  # 阻塞至有的拿
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item) # 阻塞至有地方放
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()    # 阻塞至队列中所有的元素都被接收和处理完毕。
print('All work completed')
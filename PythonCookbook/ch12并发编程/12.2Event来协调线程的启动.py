"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12.2Event来协调线程的启动.py
"""

from threading import Thread, Event
import time


# Code to execute in an independent thread
def countdown(n, start_evt):
    print('countdown starting')
    start_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
print('Coutdown is running')

# countdown starting
# T-minusCoutdown is running    主线程会等待t线程start_evt事件设置set()
#  10
# T-minus 9
# T-minus 8
# T-minus 7
# T-minus 6
# T-minus 5
# T-minus 4
# T-minus 3
# T-minus 2
# T-minus 1

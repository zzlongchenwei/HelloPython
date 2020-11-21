#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:基于线程池使用map().py
@time:2020/11/21
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures
import threading
import time

def task(n):
    print('{}: 睡眠 {}'.format(threading.current_thread().name,n))
    # time.sleep(n / 10)
    print('{}: 执行完成 {}'.format(threading.current_thread().name,n))
    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: 开始运行')
results = ex.map(task, range(5, 0, -1)) #返回值是generator 生成器
print('main: 未处理的结果 {}'.format(results))
print('main: 等待真实结果')
real_results = list(results)
print('main: 最终结果: {}'.format(real_results))


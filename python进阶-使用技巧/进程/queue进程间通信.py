#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:queue进程间通信.py
@time:2020/11/01
"""
import multiprocessing


def download_from_web(q):
    # Simulate data downloaded from the web
    data = [11, 22, 33, 44]

    # Writes data to the queue
    for temp in data:
        q.put(temp)

    print("---下载器已经下载完了数据并且存入到队列中---")


def analysis_data(q):
    """analysis data"""
    waiting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        waiting_analysis_data.append(data)

        if q.empty():
            break
    # 模拟数据处理
    print(waiting_analysis_data)


def main():
    # 1.创建一个队列
    q = multiprocessing.Queue(3)

    # 2.创建多个进程，将队列的引用当作实参
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()

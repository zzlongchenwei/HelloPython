#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:DataSegmentation.py
@time:2020/11/27
"""
# 对任意文件进行任意大小的分块
import os
import math
import time
from concurrent.futures import ThreadPoolExecutor, wait

import numpy as np
import base64


# 获得文件大小
def get_file_size(filepath):
    file_size = os.path.getsize(filepath)
    return file_size


# 根据分块数k，计算出每块数据的大小
def get_chunk_size_k(k, file_size):
    """计算块大小，并返回"""
    chunk_size = math.ceil(file_size / k)
    return chunk_size


# 根据每块大小，计算出分多少块
def get_chunk_size_chunk(chunksize, file_size):
    """计算分几块，并返回"""
    k = math.ceil(file_size / chunksize)
    return k


# 产生相应的分块文件
def create_chunk_file(file_path, read_file, num):
    # try:
    # file_name, file_format = file_path.split('.')
    # file_path = file_name + '_D' + str(num)
    # with open('{path}_D{num}'.format(path=file_path,num=num), 'wb') as subf:
    try:
        print('{path}_D{num}'.format(path=file_path, num=num))
        print(read_file)
        read_file = np.int(read_file)
        print(read_file)

        np.savetxt('{path}_D{num}'.format(path=file_path, num=num), read_file, encoding='utf-8')
        # print('file_path', file_path)
        # subf.write(read_file)
    except Exception as e:
        print('create_chunk_file分块时有问题')


def threads_split_file(k, chunk_size, file_path):
    """把文件分成k个子文件，并给序号名命"""
    try:
        with open('{path}'.format(path=file_path), 'rb') as wholef:
            with ThreadPoolExecutor() as threadpool:
                f_list = list()
                for i in range(k):
                    read_file = wholef.read(chunk_size)
                    future = threadpool.submit(create_chunk_file, file_path, read_file, i)
                    f_list.append(future)
            wait(f_list)
    except Exception as e:
        print('threads_split_file找不到要分块的文件')


# 根据大小分
def data_segmentation(file_path, n=0, k=0):
    """
    :param file_path: 文件路径
    :param n: 以多少MB分割文件，此时返回k
    :param k: 把文件分割成几份，此时返回chunk_size
    :return: k
    """
    file_size = get_file_size(file_path)
    print(file_size, 'KB')
    # chunk_size = 0
    if k:
        chunk_size = get_chunk_size_k(k, file_size)
        print(chunk_size)
        # return chunk_size
    elif n:
        chunk_size = n
        k = get_chunk_size_chunk(chunk_size, file_size)
        print(k, '块')
        # return k
    else:
        raise Exception("请设定参数：以多少MB分块(n)，或者分几块(k)")

    # t0 = time.time()
    # split_file(k, chunk_size, file_path)
    # print('运行时间',time.time()-t0)

    # time.sleep(2)
    if chunk_size and k:
        t0 = time.time()
        try:
            threads_split_file(k, chunk_size, file_path)
        except:
            print("分块错误")
        print('分块完成，thread运行时间', time.time() - t0)
        return k


if __name__ == '__main__':
    MB = 1024 * 1024
    GB = MB * 1024
    file_path = r'D:\WorkSpace\Hello-Python\ErasureCode\testfile\spiderman.jpg'
    data_segmentation(file_path, k=1000)

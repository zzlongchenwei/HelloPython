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
from concurrent.futures import ThreadPoolExecutor


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
    file_name, file_format = file_path.split('.')
    file_path = file_name + '_' + str(num)
    with open('{path}'.format(path=file_path), 'wb') as subf:
        print('file_path', file_path)

        subf.write(read_file)


# 根据分块数k，把文件分成k份
def split_file(k, chunk_size, file_path):
    """把文件分成k个子文件，并给序号名命"""
    try:
        with open('{path}'.format(path=file_path), 'rb') as wholef:
            for i in range(k):
                read_file = wholef.read(chunk_size)
                create_chunk_file(file_path, read_file, i)
    except Exception as e:
        print('文件不存在')


def threads_split_file(k, chunk_size, file_path):
    """把文件分成k个子文件，并给序号名命"""
    try:
        with open('{path}'.format(path=file_path), 'rb') as wholef:
            with ThreadPoolExecutor(max_workers=k) as threadpool:
                for i in range(k):
                    read_file = wholef.read(chunk_size)
                    threadpool.submit(create_chunk_file, file_path, read_file, i)
    except Exception as e:
        print('文件不存在')

# 根据大小分
def main(file_path):
    file_size = get_file_size(file_path)
    print(file_size, 'KB')
    # k = 65
    # chunk_size = get_chunk_size_k(k, file_size)
    # print(chunk_size / MB, 'MB')
    chunk_size = 6 * 1024 * 1024
    k = get_chunk_size_chunk(chunk_size, file_size)
    print(k, '块')

    # t0 = time.time()
    # split_file(k, chunk_size, file_path)
    # print('运行时间',time.time()-t0)

    # time.sleep(2)
    t0 = time.time()
    threads_split_file(k, chunk_size, file_path)
    print('thread运行时间',time.time()-t0)

if __name__ == '__main__':
    MB = 1024 * 1024
    GB = MB * 1024
    file_path = r'F:\WorkSpace\Hello-Python\ErasureCode\testfile\mateclass.flv'
    main(file_path)

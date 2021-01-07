#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:GenerateMatrix.py
@time:2020/11/27
"""
import base64
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

import numpy as np


# 生成一个k*k的单位矩阵
def generate_identity_matrix(k):
    identity_matrix = np.identity(k, dtype=int)
    return identity_matrix


# 生成一个k*m的范德蒙矩阵
def generate_Vandermonde(k, m):
    x = np.arange(1, m+1)
    # print(x)
    vandermonde = np.vander(x, k, increasing=True)
    return vandermonde


# 生成一个k*m的柯西矩阵
# def generate_Cauchy(k,m):
#     x = np.arange(1,k+1)


# 生成矩阵, 两个矩阵竖着拼接
def generate_generation_matrix(identity, vandermonde):
    generation_matrix = np.vstack((identity, vandermonde))
    return generation_matrix


# 打开块文件
def open_chunk_file(file_path, num):
    # file_name, file_format = file_path.split('.')
    # file_path = file_name + '_D' + str(num)
    try:
        with open('{path}_D{num}'.format(path=file_path,num=num), 'rb') as subf:
            read_file = base64.b64encode(subf.read())
            # read_file = subf.read()
            read_data = np.int64(read_file)
    except:
        print("找不到此文件")
        read_data = None
    return read_data,num

# 输入数据
def generate_data_matrix(k, file_path):
    data_list = list(range(k))
    f_list = list()
    for i in range(k):
        with ThreadPoolExecutor(max_workers=k) as threadpool:
            future = threadpool.submit(open_chunk_file, file_path, i)
            f_list.append(future)

    # 等待所有线程完成
    for future in as_completed(f_list):
        read_data, num = future.result()
        if read_data:
            data_list[num] = read_data
    # 将数组转成矩阵k*1
    data_matrix = np.mat(data_list,dtype='int64').reshape(k, 1)
    # print(data_matrix)
    return data_matrix


if __name__ == '__main__':
    k = 10
    m = 3
    file_path = r'F:\WorkSpace\Hello-Python\ErasureCode\testfile\mateclass.flv'
    identity = generate_identity_matrix(k)
    print(identity)
    vandermonde = generate_Vandermonde(k, m)
    print(vandermonde)
    # generate_data_matrix(k,file_path)

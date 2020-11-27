#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:GenerateMatrix.py
@time:2020/11/27
"""
import base64
from concurrent.futures import ThreadPoolExecutor,wait

import numpy as np

# 生成一个k*k的单位矩阵
def generate_identity_matrix(k):
    identity_matrix = np.identity(k,dtype=int)
    yield identity_matrix

# 生成一个k*m的范德蒙矩阵
def generate_Vandermonde(k,m):
    x = np.arange(1,k+1)
    # print(x)
    vandermonde = np.vander(x,m,increasing=True)
    yield vandermonde


# 生成一个k*m的柯西矩阵
# def generate_Cauchy(k,m):
#     x = np.arange(1,k+1)


# 生成矩阵, 两个矩阵竖着拼接
def generate_generation_matrix(identity,vandermonde):
    generation_matrix = np.vstack(identity,vandermonde)
    yield generation_matrix

# 打开块文件
def open_chunk_file(file_path,num,data_list):
    file_name, file_format = file_path.split('.')
    try:
        with open(file_name + '_' + str(num), 'rb') as subf:
            read_file = base64.b64encode(subf.read())
            data_list[num] = read_file
    except Exception as e:
        print('文件不存在')


# 输入数据
def generate_data_matrix(k,file_path):
    data_list = list(range(k))
    f_list = list()
    for i in range(k):
        with ThreadPoolExecutor(max_workers=k) as threadpool:
            future = threadpool.submit(open_chunk_file, file_path,i,data_list)
            f_list.append(future)

    # 等待所有线程完成
    wait(f_list)
    # 将数组转成矩阵k*1
    data_matrix = np.array(data_list).reshape(k,1)
    # print(data_matrix)
    yield data_matrix

if __name__ == '__main__':
    k = 3
    m = 3
    file_path = r'F:\WorkSpace\Hello-Python\ErasureCode\testfile\mateclass.flv'
    identity = generate_identity_matrix(k)
    print(identity)
    vandermonde = generate_Vandermonde(k,m)
    print(vandermonde)
    generate_data_matrix(k,file_path)

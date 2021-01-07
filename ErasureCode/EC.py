#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:EC.py
@time:2020/11/27
"""
from DataSegmentation import *
from GenerateMatrix import *

import numpy as np


def erasure_code_encode(k, m, file_path):
    """
    :param k: 输入数据D个数
    :param m: 生成编码值C个数
    :param file_path: 文件路径，包括文件名
    :return: 无
    """
    # 1.分割数据
    data_segmentation(file_path, k=k)
    # 2.生成矩阵C
    identity_matrix = generate_identity_matrix(k)
    vandermonde = generate_Vandermonde(k, m)
    generation_matrix = generate_generation_matrix(identity_matrix, vandermonde)
    # 3.数据矩阵D
    data_matrix = generate_data_matrix(k, file_path)
    print(data_matrix)
    # 4.生成矩阵A*输入数据D=存储数据
    store_data_matrix = np.dot(generation_matrix, data_matrix)
    # 5.存储编码值C1...Cm
    for i in range(m):
        coded_value = store_data_matrix[k+i]
        np.savetxt('{}_C{}'.format(file_path, i), coded_value)


if __name__ == '__main__':
    k = 100
    m = 3
    file_path = r'D:\WorkSpace\Hello-Python\ErasureCode\testfile\spiderman.jpg'
    erasure_code_encode(k, m, file_path)

# 2^16/8 = 8192bit
# 12*1024*8
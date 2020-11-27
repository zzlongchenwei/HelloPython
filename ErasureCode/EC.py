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

k =
file_path = r'F:\WorkSpace\Hello-Python\ErasureCode\testfile\mateclass.flv'

def erasure_code_encode(k, m, file_path):
    # 1.分割数据
    data_segmentation(file_path)
    # 2.生成矩阵
    identity_matrix = generate_identity_matrix(k)
    vandermonde = generate_Vandermonde(k, m)
    generation_matrix = generate_generation_matrix(identity_matrix, vandermonde)
    # 3.数据矩阵
    data_matrix = generate_data_matrix(k, file_path)

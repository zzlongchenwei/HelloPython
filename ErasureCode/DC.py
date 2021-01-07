#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:DC.py
@time:2020/11/28
"""
import os
import re
import base64

from GenerateMatrix import *


# 扫描已经有的文件,返回丢失的数据块号码和编码块号码
def scan_exist_file(file_path, k, m):
    """
    扫描已经有的文件,返回丢失的数据块号码和编码块号码
    :param file_path: 存放编码块的文件路径
    :param k: 数据块个数
    :param m: 编码块个数
    :return: loss_data_num, loss_coded_num
    """
    exist_list = os.listdir(file_path)
    file_name = exist_list[0].split('_')
    reg_data = re.compile(r'_D(\d+)')
    reg_coded = re.compile(r'_C(\d+)')
    exist_data_num = list()
    exist_coded_num = list()
    for i in exist_list:
        data_num = re.search(reg_data, i)
        coded_num = re.search(reg_coded, i)
        if data_num:
            exist_data_num.append(int(data_num.group(1)))
        elif coded_num:
            exist_coded_num.append(int(coded_num.group(1)))
    loss_data_num = list(set(i for i in range(k)).difference(set(exist_data_num)))
    loss_coded_num = list(set(i for i in range(m)).difference(set(exist_coded_num)))

    # 无法恢复判断
    if len(loss_data_num) > m:
        raise Exception('丢失数据块D太多')
    elif len(loss_coded_num) > len(loss_data_num):
        raise Exception('丢失编码块C太多')
    return exist_data_num, loss_data_num, exist_coded_num, loss_coded_num, file_name[0]


def new_generation_matrix(k, m, loss_data_num, loss_code_num):
    identity_matrix = generate_identity_matrix(k)
    has_delete_flag = 0
    for i in loss_data_num:
        identity_matrix = np.delete(identity_matrix, i - has_delete_flag, axis=0)  # 删除丢失数据块的行
        has_delete_flag += 1
    vandermonde = generate_Vandermonde(k, m)
    has_delete_flag = 0
    for i in loss_code_num:
        vandermonde = np.delete(vandermonde, i - has_delete_flag, axis=0)  # 删除丢失编码块的行
        has_delete_flag += 1
    if len(loss_data_num) < m:  # 如果丢失数据块个数小于m，那么只需要len(loss_data_num)行范德蒙
        has_delete_flag = 0
        for i in range(-1, -(m - len(loss_code_num) - len(loss_data_num) + 1), -1):
            vandermonde = np.delete(vandermonde, i + has_delete_flag, axis=0)  # 如只丢失一个数据块，C也丢了一块，那么就只需要删除一行，3-1-1=1
            has_delete_flag += 1
    generation_matrix = generate_generation_matrix(identity_matrix, vandermonde)
    return generation_matrix


# 求逆矩阵
def inverse_matrix(matrix):
    inverse = np.linalg.inv(matrix)
    return inverse


# 新的数据矩阵
def new_data_matrix(k, file_path, file_name, exist_data_num, exist_coded_num):
    data_list = list()
    for i in exist_data_num:
        # with open('{path}\{num}'.format(path=file_path,num=i),'rb') as existf:
        #     read_data = existf.read()
        #     data_list.append(np.int64(read_data))
        read_data = np.loadtxt('{path}\{name}_D{num}'.format(path=file_path, name=file_name, num=i))
        data_list.append(read_data)

    for i in exist_data_num:
        read_data = np.loadtxt('{path}\{name}_C{num}'.format(path=file_path, name=file_name, num=i))
        data_list.append(read_data)

    # 将数组转成矩阵k*1
    data_matrix = np.mat(data_list, dtype='int64').reshape(k, 1)
    # print(data_matrix)
    return data_matrix


# 将恢复数据矩阵分解，并恢复出原文件
def restore_original_file(retore_data_matrix, k, file_path, file_name):
    file_path = file_path + '\[new]' + file_name
    for i in range(k):
        write_data = retore_data_matrix[i]
        with open('{path}'.format(path=file_path), 'ab') as retoref:
            retoref.write(write_data)


def erasurue_code_decode(file_path, k, m):
    # 1.遍历存在的已有文件
    exist_data_num, loss_data_num, exist_coded_num, loss_coded_num, file_name = scan_exist_file(file_path, k, m)
    # 2.根据已有的文件产生新的生成矩阵
    generation_matrix = new_generation_matrix(k, m, loss_data_num, loss_coded_num)
    # 3.求逆
    inverse_generation_matrix = inverse_matrix(generation_matrix)
    # print(inverse_generation_matrix)
    # 4.新的数据矩阵
    data_matrix = new_data_matrix(k, file_path, exist_data_num, exist_coded_num)
    # 5.乘积得到恢复的数据
    restore_data_matrix = np.dot(inverse_generation_matrix, data_matrix)
    # 6.恢复文件
    restore_original_file(restore_data_matrix, k, file_path, file_name)


if __name__ == '__main__':
    file_path = r'D:\WorkSpace\Hello-Python\ErasureCode\testfile'
    k = 100
    m = 3
    erasurue_code_decode(file_path, k, m)
    # new_generation_matrix(k, m, loss_code_num=[], loss_data_num=[3, 5, 7])

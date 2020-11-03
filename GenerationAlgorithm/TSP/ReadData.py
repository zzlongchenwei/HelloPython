#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:ReadData.py
@time:2020/11/02
"""
import csv
from collections import defaultdict

def read_city_data(filename):
    """
    description: 读取城市信息的csv文件
    param filename:  csv格式文件名
    return: city_data键为城市号，值为xy坐标
    """
    with open(filename, newline='') as csvfile:
        city_data = defaultdict(list)
        city_reader = csv.reader(csvfile)
        header = 1
        for row in city_reader:
            if header: header = 0
            else:
                city_data[int(row[0])].append(float(row[1]))
                city_data[int(row[0])].append(float(row[2]))
        return city_data


if __name__ == '__main__':
    # 测试
    city_data = read_city_data('city_coordinate.csv')
    print(city_data)
    for city, coord in city_data.items():
        print(city, coord)
    print(len(city_data))
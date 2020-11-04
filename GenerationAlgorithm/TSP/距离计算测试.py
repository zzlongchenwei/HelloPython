#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:距离计算测试.py
@time:2020/11/02
"""
import math
from ReadData import *

city_data = read_city_data('city_coordinate.csv')

def distance_between_two_city(city1_coord, city2_coord):
    # 法1. 距离公式
    distance_2point = math.dist(city1_coord, city2_coord)
    return distance_2point

if __name__ == '__main__':
    # line = [7, 13, 8, 11, 9, 10, 1, 2, 14, 3, 4, 5, 6, 12]
    line = [8, 13, 7, 12, 6, 5, 4, 3, 14, 2, 1, 10, 9, 11]
    now_city= line[0]
    cirle_distance = 0
    for i in line[1:]:
        old_city = now_city
        now_city = i
        cirle_distance += distance_between_two_city(city_data[old_city],city_data[now_city])
    cirle_distance += distance_between_two_city(city_data[now_city],city_data[line[0]])
    print(cirle_distance)
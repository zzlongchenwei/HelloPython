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
    c1 = city_data[14]
    c2 = city_data[2]
    print(distance_between_two_city(c1,c2))
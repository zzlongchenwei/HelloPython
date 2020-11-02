#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:父代选择测试.py
@time:2020/11/02
"""
import random

def choose_parent(copy_individual):
    # copy_individual原种群的深拷贝后的个体
    parent = list() # 创建一个parent列表
    city_size = len(copy_individual)-1
    print('city_size1',city_size)
    if city_size != -1:
        n1 = random.randint(0, city_size)  # 随机产生一个0~city_size-1的整数
        parent.append(copy_individual.pop(n1))  # 推出这个城市
        city_size -= 1
        print('city_size2', city_size)
        n2 = random.randint(0, city_size)
        parent.append(copy_individual.pop(n2))
        city_size -= 1
        print('city_size3', city_size)
    return parent

if __name__ == '__main__':
    l = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    print(len(l))
    while len(l):
        print(choose_parent(l))

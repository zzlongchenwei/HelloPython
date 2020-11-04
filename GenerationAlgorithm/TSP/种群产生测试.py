#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:种群产生测试.py
@time:2020/11/04
"""
import random


def produce_pop(city_size,pop_size,pop):
    range_list = list(range(1, city_size + 1))  # 生成一个列表，[1,x,x,x,..,city_num]
    for i in range(pop_size):  # 遍历pop_size次
        pop.append(random.sample(range_list, k=city_size))  # 每次从range_list抽样city_num个

if __name__ == '__main__':
    pop = list()
    produce_pop(14,30,pop)
    print(pop)
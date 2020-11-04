#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:变异测试.py
@time:2020/11/04
"""
import random


def mutation(pop_size, city_size, new_pop, pm=1):  # pm为变异概率 0.001~0.1
    for i in range(pop_size):
        if random.random() < pm:
            # a. 随机产生一个变异位置
            X = Y = 0
            while X == Y:
                X = random.randint(0, city_size - 1)  # 变异位置从1到city_size-1
                print('x:', X)
                Y = random.randint(0, city_size - 1)
                print('y:', Y)
            new_pop[i][X], new_pop[i][Y] = new_pop[i][Y], new_pop[i][X]  # 交换两个位置
            print(new_pop)


if __name__ == '__main__':
    pop_size = 2
    city_size = 3
    new_pop = [[1, 2, 3], [4, 5, 6]]
    mutation(pop_size, city_size, new_pop)

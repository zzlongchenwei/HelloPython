#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:main.py
@time:2020/10/30
"""
from tspGA import GA
from tspPlot import *
from ReadData import *

if __name__ == '__main__':
    city_data = read_city_data('city_coordinate.csv')
    # 1. 实例化TSP遗传算法
    ga = GA(city_data, city_size=14, pop_size=300, NG=300)   # 种群大的话容易产生最优解

    # 2. 产生种群
    ga.produce_pop()
    # 上一个种群的适应度
    ga.old_fitness_calculation()
    # print('初始种群：', ga.pop)
    # print('初始种群旅行一圈的距离:',ga.old_pop_fitness)
    avg_pop_fitness = list()

    while ga.stop_rule():
        # 3. OX交叉
        ga.crossover(pc=0.4)

        # 4. 变异
        ga.mutation(pm=1)

        # 5. 选择
        # 5.1 计算适应度
        ga.fitness_calculation()
        # 5.2 选择
        ga.selection()

        # 6. 更新种群
        ga.update_pop()
        ga.age += 1

        # 每代平均
        avg_pop_fitness.append(sum(ga.old_pop_fitness)/ga.pop_size)

    print('======>迭代第%s完成' % ga.age)
    print('当前种群为', ga.pop)
    print('适应度为', ga.old_pop_fitness)
    print('最短距离:', min(ga.old_pop_fitness),'怎么走:', ga.pop[ga.old_pop_fitness.index(min(ga.old_pop_fitness))])
    plot_fit(avg_pop_fitness)

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:main.py
@time:2020/10/30
"""

from tspGA import GA
from ReadData import *

city_data = read_city_data('city_coordinate.csv')

if __name__ == '__main__':
    # 1. 实例化TSP遗传算法
    ga = GA(city_size=14)

    # 2. 产生种群
    ga.produce_pop()
    print('初始种群：', ga.pop)
    ga.init_pop_fitness(city_data)
    print('初始种群旅行一圈的距离:',ga.old_pop_fitness)

    while ga.stop_rule():
        # 3. 交叉
        ga.crossover(pc=0.4)
        print('======>交叉完成:', ga.new_pop)

        # 4. 变异
        ga.mutation()
        print('=====>变异完成:', ga.new_pop)

        # 5. 选择
        # 5.1 计算适应度
        ga.fitness_calculation(city_data)
        print('旅行一圈的距离:', ga.pop_fitness)
        # 5.2 选择
        ga.selection()
        print('=====>选择完成:', ga.choice_pop)

        # 6. 更新种群
        ga.update_pop()

        ga.age += 1

    print('======>迭代第%s完成' % ga.age)
    print('当前种群为', ga.pop)
    print('适应度为', ga.old_pop_fitness)
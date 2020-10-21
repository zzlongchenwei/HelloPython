"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:main.py
"""

from population import Population
from selection import Selection

interval = [-10, 10]    # 区间
mod = 'min'     # 模式


def func(x):
    return x**2


ga = Population(func, mod, interval, 20)    # 一个种群实例
ga.produce_rpop()   # 创建一个是实数编码种群
print('当前种群', ga.pop)   # 打印该种群
print('----'*10)

ga.crossover()
print('交叉后', ga.new_pop)
print('----'*10)

ga.pro_fitness(1)  # 计算适应值
print('种群适应度列表', ga.pop_fitness)   # 打印种群适应度列表
print('----'*10)
ga.rws()
print('----'*10)


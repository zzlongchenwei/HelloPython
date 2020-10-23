"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:main.py
"""

from population import Population
from stopping_rule import stop_rule

interval = [-10, 10]  # 区间
mod = 'min'  # 模式


def func(x):
    return x ** 2


# 产生一个种群
ga = Population(func, mod, 1, interval, 20)  # 一个种群实例
ga.produce_rpop()  # 创建一个是实数编码种群
# print('当前种群', ga.pop)  # 打印该种群
# print('----' * 10)
while stop_rule(ga.age, NG=150):
    print('第%s代' % ga.age)
    print('当前种群', ga.pop)
    print('-----' * 10)

    # 交叉
    ga.crossover(op_alph=1)
    print('----' * 10)

    # 变异
    ga.mutation()
    print('----' * 10)

    # 选择
    ga.pro_fitness()  # 计算适应值

    print('----' * 10)
    ga.rws()  # 轮盘赌选择
    print('----' * 10)

    # 更新种群
    ga.update_pop()

    ga.age += 1

print('迭代%s完成' % ga.age)
sort_lits = sorted(map(abs, ga.pop))
print('排序后', sort_lits)
min = func(sort_lits[0])
print('最优解', sort_lits[0])
print('最优值', min)

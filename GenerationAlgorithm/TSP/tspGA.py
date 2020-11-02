#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:tspGA.py
@time:2020/10/28
"""
import random
import copy


class GA:
    """
    generation algorithm
    """
    def __init__(self, city_num, pop_size=20):
        self.pop_size = pop_size  # 种群大小
        self.city_num = city_num    # 城市个数

        self.pop = []  # 种群集合
        self.new_pop = []  # 新的种群集合
        self.choice_pop = []  # 选择后的种群集合

        self.pop_fitness = []  # 适应度集合
        self.pisl = []  # 选择概率集合

        self.age = 1  # 迭代数

    # gauss
    def gauss_perturbation(self,miu=0,sigma=1, ab=0): # gauss扰动
        if ab:
            return abs(random.gauss(miu, sigma))
        else:
            return random.gauss(miu, sigma)

    # ---------------
    #      种群
    # ---------------
    # 种群生成
    def produce_pop(self):
        range_list = list(range(self.city_num))
        for i in range(self.pop_size):
            self.pop.append(random.sample(range_list, k=self.city_num))

        print('初始种群：', self.pop)

    # 种群更新
    def update_pop(self):
        self.pop = self.new_pop
        self.new_pop = []
        self.choice_pop = []
        self.pop_fitness = []
        self.pisl = []

    # -------------
    #     选择
    # -------------
    # 适应度计算
    def pro_fitness(self):
        pass

    # 选择函数
    def selection(self):
        pass

    # -------------
    #     交叉
    # -------------
    def crossover(self, pc=0.4):
        # pc为交叉概率 0.4~0.9
        pass

    # -------------
    #     变异
    # -------------
    def mutation(self, pm=0.01):  # pm为变异概率 0.001~0.1
        pass

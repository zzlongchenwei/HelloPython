"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:Population.py
"""
import random
from selection import Selection
from genetic_operators import GenOperators


class Population(Selection, GenOperators):
    """
    种群的生成 produce_bpop()  produce_rpop()
    种群的更新 update_pop()
    """

    def produce_bpop(self):
        # 产生二进制编码初始种群
        DNA = []
        for i in range(self.pop_size):
            for j in range(self.DNAlen):
                DNA.append(random.randint(0, 1))
            self.pop.append(DNA)
            DNA = []

    def produce_rpop(self):
        # 产生实数编码种群
        for i in range(self.pop_size):
            self.pop.append(random.uniform(self.interval[0], self.interval[-1]))

    def update_pop(self):
        # 更新种群
        self.pop = self.new_pop
        self.new_pop = []
        self.choice_pop = []
        self.pop_fitness = []
        self.pisl = []
        print('——————更新种群——————')


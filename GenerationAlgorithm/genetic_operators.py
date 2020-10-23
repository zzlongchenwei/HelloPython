"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:genetic_operators.py
"""
from GA import GAbase
import random
import copy


class GenOperators(GAbase):
    # 交叉
    def crossover(self, pc=0.4, mode=0, op_alph=0):
        # pc为交叉概率 0.4~0.9
        # mode=0 算术交叉
        parent = [0, 0]
        m = self.pop_size-1
        temp = copy.deepcopy(self.pop)
        while True:
            n1 = random.randint(0, m)
            parent[0] = temp.pop(n1)
            m -= 1
            n2 = random.randint(0, m)
            parent[1] = temp.pop(n2)
            m -= 1

            # mode=0 算术交叉  alph默认1/2
            if mode == 0:
                rnum = random.random()
                if op_alph:
                    alph = random.random()
                else:
                    alph= 0.5
                if 0 <= rnum <= pc:
                    new_individual1 = alph*parent[0] + (1-alph)*parent[1]
                    new_individual2 = alph*parent[1] + (1-alph)*parent[0]
                    self.new_pop.append(new_individual1)
                    self.new_pop.append(new_individual2)
                else:
                    self.new_pop.append(parent[0])
                    self.new_pop.append(parent[1])

            if m == -1:
                print('-----交叉完成-----')
                print('交叉后列表', self.new_pop)
                break

    # 变异
    def mutation(self, pm=0.01):  # pm为变异概率 0.001~0.1
        for i in range(self.pop_size):
            rnum = random.random()
            if rnum <= pm:
                self.new_pop[i] = random.uniform(self.interval[0], self.interval[1])
        print('-----变异完成-----')
        print('变异后列表', self.new_pop)





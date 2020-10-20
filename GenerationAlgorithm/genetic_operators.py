"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:genetic_operators.py
"""


class Crossover:
    """
    交叉
    """
    def __init__(self, Pc):
        self.crossover_prob = Pc

    def single_point(self):
        pass


class Mutation:
    """
    变异
    """
    def __init__(self, Pm):
        self.mutation_prob = Pm

    def binary_mutate(self):
        pass
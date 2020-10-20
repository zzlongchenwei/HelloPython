"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:Population.py
"""
import random


class Population:
    """
    种群的构建
    种群的编码方式
    resolution 要求的精度，小数点后几位，（默认为1，小数点后0位）
    interval 取值区间
    """
    def __init__(self, pop_size, interval, resolution=0):

        self.pop_size = pop_size    # 种群大小
        self.res = resolution   # 要求的精度 小数点后几位
        self.interval = interval   # 区间
        self.DNAlen = self._DNA_lenth()  # DNA长度

        self.pop = []   # 种群集合
        self.new_pop = []   # 新的种群集合
        self.pop_fitness = [] # 个体适应度集合

    def _DNA_lenth(self):
        # 根据精度和区间计算出需要多长二进制位来编码
        L = self.interval[-1] - self.interval[0]    # 区间长度
        sumdiv = L*(10**self.res)   # 把区间总共划分位多少块
        DNAl = 0 # DNA长度
        while True:
            sup = 2 ** DNAl
            if sup < sumdiv:
                DNAl += 1
            else:
                break
        return DNAl

    def produce_pop(self):
        # 产生二进制初始种群
        DNA = []
        for i in range(self.pop_size):
            for j in range(self.DNAlen):
                DNA.append(random.randint(0, 1))
            self.pop.append(DNA)
            DNA = []

    def update_pop(self):
        # 更新种群
        pass


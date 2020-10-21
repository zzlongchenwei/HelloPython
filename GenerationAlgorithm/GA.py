"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:GA.py
"""
import random


class GAbase:
    """
    generation algorith base
    pop_size 种群大小
    resolution 要求的精度，小数点后几位，（默认为1，小数点后0位）
    interval 取值区间
    """
    def __init__(self, func, mod, interval, pop_size=20, resolution=0):
        self.func = func  # 原函数
        self.mod = mod  # 模式

        self.pop_size = pop_size  # 种群大小
        self.res = resolution  # 要求的精度 小数点后几位
        self.interval = interval  # 区间
        self.DNAlen = self._DNA_lenth()  # DNA长度

        self.pop = []  # 种群集合
        self.new_pop = []  # 新的种群集合

        self.pop_fitness = []  # 适应度集合

    def _DNA_lenth(self):
        # 根据精度和区间计算出需要多长二进制位来编码
        L = self.interval[-1] - self.interval[0]  # 区间长度
        sumdiv = L * (10 ** self.res)  # 把区间总共划分位多少块
        DNAl = 0  # DNA长度
        while True:
            sup = 2 ** DNAl  # sup为2的DNA长度次方
            if sup < sumdiv:
                DNAl += 1
            else:
                break
        return DNAl  # 返回DNA长度

    @classmethod
    def sigma(cls):
        return abs(random.gauss(0, 1))

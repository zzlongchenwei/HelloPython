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
    func 原函数
    mod 模式 ['min' 最小值], ['max' 最大值]
    scal 标定方法 [0：原函数为适应值函数]  [1：线性标定]
    interval 取值区间
    pop_size 种群大小
    resolution 要求的精度，小数点后几位，（默认为1，小数点后0位）
    """
    def __init__(self, func, mod, scal, interval, pop_size=20, resolution=0):
        self.func = func  # 原函数
        self.mod = mod  # 模式
        self.scal = scal # 标定模式

        self.pop_size = pop_size  # 种群大小

        self.res = resolution  # 要求的精度 小数点后几位
        self.interval = interval  # 区间
        self.DNAlen = self._DNA_lenth()  # DNA长度

        self.pop = []  # 种群集合
        self.new_pop = []  # 新的种群集合
        self.choice_pop = []    # 选择后的种群集合

        self.pop_fitness = []  # 适应度集合
        self.pisl = [] # 选择概率集合

        self.age = 1 # 迭代数

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
    def sigma(cls, ab=0):
        if ab:
            return abs(random.gauss(0, 1))
        else:
            return random.gauss(0, 1)


if __name__ == '__main__':
    print(GAbase.sigma())

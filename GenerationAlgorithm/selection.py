"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:selection.py
"""


class Selection:
    """
    选择策略：选择适应度高的个体。
    --------------------------
    计算适应度函数
    pro_fitness() 按比例的适应度计算
    --------------------------
    选择函数
    rws() 轮盘赌选择
    """
    def __init__(self,func):
        self.func = func

    # 标定
    def scaling_fit(self, pop):
        valuelist = []    # 函数值列表
        for i in range(len(pop)):
            valuelist.append(self.func(pop[i]))
        fmax = max(valuelist)
        F = -self.func + fmax + sigema
    # 适应度计算
    def pro_fitness_(self):
        # proportional_fitness_assignment 按比例的适应度计算

        pass

# 选择函数
    def rws(self):
        # roulette_wheel_selection() 轮盘赌选择
        pass



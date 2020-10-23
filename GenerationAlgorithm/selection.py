"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:selection.py
"""

from GA import GAbase
import random

class Selection(GAbase):
    """
    选择策略：选择适应度高的个体。
    --------------------------
    计算适应度函数
    pro_fitness() 按比例的适应度计算
    --------------------------
    选择函数
    rws() 轮盘赌选择
    """

    # 线性标定
    def line_scaling_fit(self, valuelist,a=1, b=0):  # valuelist原函数值列表
        if self.mod == 'max':
            fm = min(valuelist)
            print('当前代最小值', fm)
            for i in range(len(valuelist)):  # 遍历原函数值列表，
                if valuelist[i] > fm:
                    scalf = a*(valuelist[i] - fm) + b + random.random()
                    self.pop_fitness.append(scalf)
                else: self.pop_fitness.append(GAbase.sigma(1))

        elif self.mod == 'min':
            fm = max(valuelist)
            print('当前待最大值', fm)
            for i in range(len(valuelist)):  # 遍历原函数值列表，
                if valuelist[i] < fm:   # 如果该值比当前代最大个体值都小，就将该值加入种群适应度
                    scalf = a*(fm - valuelist[i]) + b
                    self.pop_fitness.append(scalf)
                else: self.pop_fitness.append(GAbase.sigma(1))    # 否则加入一个适应度特别小的值
        print('种群适应度列表', self.pop_fitness)  # 打印种群适应度列表

    # 适应度计算
    def pro_fitness(self):
        # proportional_fitness_assignment 按比例的适应度计算
        # scal = 0 原函数标定
        # scal = 1 线性标定下的适应度

        valuelist = []    # 函数值列表
        for i in range(self.pop_size):
            x = self.new_pop[i]
            f = self.func(x)
            valuelist.append(f)     # 调用原函数对pop里的每个数进行计算添加到valuelist中
        print('函数值列表', valuelist)
        if self.scal == 0:
            self.pop_fitness = valuelist    # 用原函数算适应值
        elif self.scal == 1:
            self.line_scaling_fit(valuelist)

    def accnum(self):   # 计算累计值
        # 累计值
        acc = 0
        accpis = self.pisl
        for i in range(self.pop_size):
            accpis[i] = acc + accpis[i]
            acc = accpis[i]
        accpis.append(0)    # 把0添加到末尾，因为i=0 时， 0-1=-1
        print('累计概率', self.pisl)

    # 选择函数: rws()轮盘赌选择
    def rws(self):
        # roulette_wheel_selection() 轮盘赌选择
        # 计算选择率
        total_fit = sum(self.pop_fitness)
        print('适应度总和', total_fit)

        for i in range(self.pop_size):
            pis = self.pop_fitness[i] / total_fit   # 单个选择概率
            self.pisl.append(pis)
        print('选择概率', self.pisl)
        print('总选择概率', sum(self.pisl))

        # 计算累计值
        self.accnum()
        # print(pisl)

        # 轮盘选择
        choice_num = []
        i = 0
        flag = 1
        num = 0
        while True:
            if flag:
                num = random.random()
                # print(num)
            if self.pisl[i - 1] <= num < self.pisl[i]:    # 看随机数位于累计值得哪个区间内 如：0__1__*__2__3_____4
                choice_num.append(i)            # 如果落在区间内就把几号加入选择列表里
                flag = 1    # 并开启下一轮随机数选择
                i = 0   # 从头匹配
            else:
                i += 1  # 进如下一个区间
                flag = 0    # 不产生新的随机数
            if i == self.pop_size:
                i = 0
            if len(choice_num) == self.pop_size:
                print('-----轮盘选择结束-----')
                break  # 直到选择够了种族个数
        print('选择的是', choice_num)

        for j in range(self.pop_size):
            n = choice_num[j]
            self.choice_pop.append(self.new_pop[n])






















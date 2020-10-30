"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:Population.py
"""
import random
import copy
from collections import defaultdict

class GA:
    """
      generation algorithm
      func 原函数
      mod 模式 ['min' 最小值], ['max' 最大值]
      scal 标定方法 [0：原函数为适应值函数]  [1：线性标定]
      interval 取值区间
      pop_size 种群大小
      resolution 要求的精度，小数点后几位，（默认为1，小数点后0位）
      NG 最大迭代次数
      """

    def __init__(self, func, mod, scal, interval, NG, pop_size=20, resolution=0):
        self.func = func  # 原函数
        self.mod = mod  # 模式
        self.scal = scal  # 标定模式

        self.pop_size = pop_size  # 种群大小

        # self.res = resolution  # 要求的精度 小数点后几位
        self.interval = interval  # 区间
        # self.DNAlen = self._DNA_lenth()  # DNA长度

        self.pop = []  # 种群集合
        self.new_pop = []  # 新的种群集合
        self.choice_pop = []  # 选择后的种群集合

        self.now_best_individual = []
        self.now_best_func = []

        self.pop_fitness = []  # 适应度集合
        self.pisl = []  # 选择概率集合

        self.age = 0  # 迭代数
        self.num_gen = NG # 最大迭代次数

    # 根据精度和区间计算出需要多长二进制位来编码
    # def _DNA_lenth(self):
    #     L = self.interval[-1] - self.interval[0]  # 区间长度
    #     sumdiv = L * (10 ** self.res)  # 把区间总共划分位多少块
    #     DNAl = 0  # DNA长度
    #     while True:
    #         sup = 2 ** DNAl  # sup为2的DNA长度次方
    #         if sup < sumdiv:
    #             DNAl += 1
    #         else:
    #             break
    #     return DNAl  # 返回DNA长度

    # gauss
    def gauss_perturbation(self,miu=0,sigma=1, ab=0): # gauss扰动
        if ab:
            return abs(random.gauss(miu, sigma))
        else:
            return random.gauss(miu, sigma)

    # -------------
    #   种群生成
    # ---------------
    # 产生二进制编码初始种群
    # def produce_bpop(self):
    #     DNA = []
    #     for i in range(self.pop_size):
    #         for j in range(self.DNAlen):
    #             DNA.append(random.randint(0, 1))
    #         self.pop.append(DNA)
    #         DNA = []

    # 产生实数编码种群
    def produce_rpop(self):
        for i in range(self.pop_size):
            self.pop.append(random.uniform(self.interval[0], self.interval[-1]))

    # 更新种群
    def update_pop(self):
        self.pop = self.new_pop
        self.new_pop = []
        self.choice_pop = []
        self.pop_fitness = []
        self.pisl = []

    # 最优值
    def optimized_value(self):
        optimal_value = ()
        # defaultdict方法创建字典
        pop_v_k = defaultdict(list) # 键为列表
        for x in self.pop:
            pop_v_k[x].append(self.func(x))
            # pop_v_k[x].setdefault(str(x), self.func(x))
        if self.mod == 'min':
            optimal_value = min(zip(pop_v_k.values(), pop_v_k.keys()))   # zip返回一个元组迭代器，
        return optimal_value

    # ------------
    #   选择
    # -------------
    # 线性标定
    def line_scaling_fit(self, valuelist, a=1, b=0):  # valuelist原函数值列表
        if self.mod == 'max':
            fm = min(valuelist)
            print('当前代最小值', fm)
            for i in range(len(valuelist)):  # 遍历原函数值列表，
                if valuelist[i] > fm:
                    scalf = a * (valuelist[i] - fm) + b
                    self.pop_fitness.append(scalf)
                else:
                    self.pop_fitness.append(self.gauss_perturbation(1))
        elif self.mod == 'min':
            fm = max(valuelist)
            print('当前待最大值', fm)
            for i in range(len(valuelist)):  # 遍历原函数值列表，
                if valuelist[i] < fm:  # 如果该值比当前代最大个体值都小，就将该值加入种群适应度
                    scalf = a * (fm - valuelist[i]) + b
                    self.pop_fitness.append(scalf)
                else:
                    self.pop_fitness.append(self.gauss_perturbation(1))  # 否则加入一个适应度特别小的值
        print('种群适应度列表', self.pop_fitness)  # 打印种群适应度列表

    # 适应度计算
    def pro_fitness(self):
        # proportional_fitness_assignment 按比例的适应度计算
        # scal = 0 原函数标定
        # scal = 1 线性标定下的适应度

        valuelist = []  # 函数值列表
        for i in range(self.pop_size):
            x = self.new_pop[i]
            f = self.func(x)
            valuelist.append(f)  # 调用原函数对pop里的每个数进行计算添加到valuelist中
        print('函数值列表', valuelist)
        if self.scal == 0:
            self.pop_fitness = valuelist  # 用原函数算适应值
        elif self.scal == 1:
            self.line_scaling_fit(valuelist)

    # 计算累计值
    def accnum(self):
        # 累计值
        acc = 0
        accpis = self.pisl
        for i in range(self.pop_size):
            accpis[i] = acc + accpis[i]
            acc = accpis[i]
        accpis.append(0)  # 把0添加到末尾，因为i=0 时， 0-1=-1
        # print('累计概率', self.pisl)

    # 选择函数
    # rws()轮盘赌选择
    def rws(self, percent_size):
        # roulette_wheel_selection() 轮盘赌选择
        # 计算选择率
        total_fit = sum(self.pop_fitness)
        # print('适应度总和', total_fit)

        for i in range(self.pop_size):
            pis = self.pop_fitness[i] / total_fit  # 单个选择概率
            self.pisl.append(pis)
        # print('选择概率', self.pisl)
        # print('总选择概率', sum(self.pisl))

        # 计算累计值
        self.accnum()
        # print(pisl)

        # 轮盘选择  # 精英选择
        choice_num = []
        i = 0
        flag = 1
        num = 0
        while True:
            if flag:
                num = random.random()
                # print(num)
            if self.pisl[i - 1] <= num < self.pisl[i]:  # 看随机数位于累计值得哪个区间内 如：0__1__*__2__3_____4
                choice_num.append(i)  # 如果落在区间内就把几号加入选择列表里
                flag = 1  # 并开启下一轮随机数选择
                i = 0  # 从头匹配
            else:
                i += 1  # 进如下一个区间
                flag = 0  # 不产生新的随机数
            if i == self.pop_size:
                i = 0
            if len(choice_num) == percent_size:
                break  # 直到选择够了种族个数
        # print('选择的是', choice_num)

        for j in range(percent_size):
            n = choice_num[j]
            self.choice_pop.append(self.new_pop[n])
        print('轮盘选择的', self.choice_pop[self.pop_size-percent_size:])


    # elit retention 精英保留
    def elit_retention(self, percent_size:int):
        sortfit_num = sorted(range(self.pop_size), key=lambda k:self.pop_fitness[k])
        print('按适应度值排的序号', sortfit_num)
        for i in range(percent_size):
            n = sortfit_num[i]
            self.choice_pop.append(self.new_pop[n])
        print('精英选择的', self.choice_pop)

    def selection(self, percent_size):
        self.elit_retention(percent_size)
        self.rws(self.pop_size-percent_size)
        print('选择的是', self.choice_pop)
    # ------------
    #   交叉
    # -------------
    def crossover(self, pc=0.4, mode=0, op_alph=0):
        # pc为交叉概率 0.4~0.9
        # mode=0 算术交叉
        parent = [0, 0]
        m = self.pop_size - 1
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
                    alph = 0.5
                if 0 <= rnum <= pc:
                    new_individual1 = alph * parent[0] + (1 - alph) * parent[1]
                    new_individual2 = alph * parent[1] + (1 - alph) * parent[0]
                    self.new_pop.append(new_individual1)
                    self.new_pop.append(new_individual2)
                else:
                    self.new_pop.append(parent[0])
                    self.new_pop.append(parent[1])

            if m == -1:
                print('-----交叉完成-----')
                print('交叉后列表', self.new_pop)
                break

    # ------------
    #   变异
    # -------------
    def mutation(self, mod, pm=0.005):  # pm为变异概率 0.001~0.1   # 高斯变异
        for i in range(self.pop_size):
            flag = 1
            rnum = random.random()
            if rnum <= pm:
                while flag:     # 这个变异值在区间内才允许
                    if mod == 'uniform':
                        self.new_pop[i] = random.uniform(self.interval[0], self.interval[1])
                    elif mod == 'gauss':
                        self.new_pop[i] = self.gauss_perturbation(miu=self.new_pop[i], sigma=1)

                    if self.interval[0] <= self.new_pop[i] or self.interval[1] <= self.new_pop[i]:
                        flag = 0


        print('-----变异完成-----')
        print('变异后列表', self.new_pop)

    # ------------
    #   停止条件
    # -------------
    def stop_rule(self):  # NG最大迭代数 100~500
        # 满足最大迭代次数时停止
        if self.age == self.num_gen:
            return 0
        else:
            return 1

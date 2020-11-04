#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:tspGA.py
@time:2020/10/28
"""
import random
import math
import copy
# import numpy as np


class GA:
    """
    generation algorithm
    """
    def __init__(self, city_data, city_size, pop_size=20, NG=150):
        self.pop_size = pop_size  # 种群大小
        self.city_size = city_size    # 城市个数
        self.city_data = city_data  # 城市的数据

        self.pop = []  # 种群集合
        self.new_pop = []  # 新的种群集合，交叉后，变异后
        self.choice_pop = []  # 选择后的种群集合
        self.pop_fitness = []  # 适应度集合
        self.old_pop_fitness = [] # 上一代适应度集合

        self.age = 0  # 迭代数
        self.num_gen = NG  # 最大迭代次数

    # ---------------
    #      种群
    # ---------------
    # 种群生成
    def produce_pop(self):
        range_list = list(range(1, self.city_size+1))    # 生成一个列表，[1,x,x,x,..,city_num]
        for i in range(self.pop_size):      # 遍历pop_size次
            self.pop.append(random.sample(range_list, k=self.city_size))     # 每次从range_list抽样city_num个

    # 种群更新
    def update_pop(self):
        self.pop = self.choice_pop

        # 更新老种群适应度
        # self.old_pop_fitness = self.pop_fitness
        self.old_pop_fitness = []
        self.old_fitness_calculation()

        # 为下一次迭代清空
        self.new_pop = []
        self.choice_pop = []
        self.pop_fitness = []

    # -------------
    #     交叉
    # -------------
    # 选俩父代
    def choose_parent(self, copy_pop):
        # copy_individual原种群的深拷贝后的个体
        parent = list()  # 创建一个parent列表
        city_size = len(copy_pop) - 1
        if city_size != -1:
            n1 = random.randint(0, city_size)  # 随机产生一个0~city_size-1的整数
            parent.append(copy_pop.pop(n1))  # 推出这个城市
            city_size -= 1
            n2 = random.randint(0, city_size)   # 随机产生一个0~city_size-2
            parent.append(copy_pop.pop(n2))
        return parent


    # 交叉
    def crossover(self,pc=0.4):  # pc为交叉概率 0.4~0.9
        """
        Order Crossover顺序交叉
        a. 选取切点X,Y
        b. 交换中间部分
        c. 从 第二个切点Y 后第一个基因起列出原顺序，去掉已有基因
        d. 从 第二个切点Y 后第一个位置起，将获得无重复顺序填入
        """
        copy_pop = copy.deepcopy(self.pop)  # 深拷贝一份种群

        # a.选取切点X,Y
        X = 14 // 3
        Y = -X

        while len(copy_pop):
            # 父代选择
            parent = self.choose_parent(copy_pop)

            if random.random() < pc:    # 如果小于交叉概率就交叉
                # c. 从 第二个切点Y 后第一个基因起列出原顺序，去掉已有基因
                # 列出原顺序
                sequence0 = parent[0][Y:] + parent[0][:X] + parent[0][X:Y]
                sequence1 = parent[1][Y:] + parent[1][:X] + parent[1][X:Y]

                # b. 交换中间部分
                parent[0][X:Y], parent[1][X:Y] = parent[1][X:Y], parent[0][X:Y]

                # c. 从 第二个切点Y 后第一个基因起列出原顺序，去掉已有基因
                # 列出原顺序
                # sequence0 = parent[0][Y:] + parent[0][:X] + parent[0][X:Y]
                # sequence1 = parent[1][Y:] + parent[1][:X] + parent[1][X:Y]

                # 去掉已有基因
                for i in parent[0][X:Y]:  # 遍历中间交换部分
                    if i in sequence0:  # 如果i在原序列中
                        sequence0.remove(i)  # 就去掉这个值

                for i in parent[1][X:Y]:  # 遍历中间交换部分
                    if i in sequence1:  # 如果i在原序列中
                        sequence1.remove(i)  # 就去掉这个值

                # d. 从 第二个切点Y 后第一个位置起，将获得无重复顺序填入
                parent[0][Y:] = sequence0[:X]
                parent[0][:X] = sequence0[X:]

                parent[1][Y:] = sequence1[:X]
                parent[1][:X] = sequence1[X:]

                self.new_pop.append(parent[0])
                self.new_pop.append(parent[1])
            else:   # 否则不交叉
                self.new_pop.append(parent[0])
                self.new_pop.append(parent[1])

    # -------------
    #     变异
    # -------------
    def mutation(self, pm=0.01):  # pm为变异概率 0.001~0.1
        for i in range(self.pop_size):
            if random.random() < pm:
                # a. 随机产生一个变异位置
                X = random.randint(1,self.city_size-1)  # 变异位置从1到city_size-1
                self.new_pop[i][X-1], self.new_pop[i][X] = self.new_pop[i][X], self.new_pop[i][X-1]     # 交换两个位置

    # -------------
    #     选择
    # -------------
    # 计算距离
    def distance_between_two_city(self, city1_coord, city2_coord):
        # 法1. 距离公式
        distance_2point = math.dist(city1_coord, city2_coord)
        return distance_2point

        # 法2. 利用向量
        # city1_array = np.array(city1_coord)     # 将一个城市的坐标转换为向量
        # city2_array = np.array(city2_coord)
        # between_array = city2_array - city1_array
        # distance_2point = math.hypot(between_array)     # 二范数
        # return distance_2point

    # 适应度计算
    def fitness_calculation(self):
        for i in range(self.pop_size):  # 遍历所有个体
            now_city = self.new_pop[i][0]   # 现在所在的城市是个体的第一个城市
            travel_num = 1  # 旅行了几个城市了
            circle_distance = 0     # 旅游一圈的距离
            for city_number in self.new_pop[i][1:]:
                pre_city = now_city     # 上个城市等于没更新前的now_city
                now_city = city_number  # 更新now_city
                circle_distance += self.distance_between_two_city(self.city_data[pre_city],
                                                                  self.city_data[now_city]) # 计算两点距离
                travel_num += 1     # 又旅行了一个城市
                if travel_num == self.city_size:    # 如果旅行了self.city_size个城市了，就该回到出发的地方
                    circle_distance += self.distance_between_two_city(self.city_data[self.new_pop[i][-1]],
                                                                      self.city_data[self.new_pop[i][0]])

            self.pop_fitness.append(circle_distance)


    # 计算老种群的旅行距离
    def old_fitness_calculation(self):
        for i in range(self.pop_size):  # 遍历所有个体
            circle_distance = 0  # 旅游一圈的距离
            now_city = self.pop[i][0]  # 现在所在的城市是个体的第一个城市
            for city_number in self.pop[i][1:]:
                pre_city = now_city  # 上个城市等于没更新前的now_city
                now_city = city_number  # 更新now_city
                circle_distance += self.distance_between_two_city(self.city_data[pre_city],
                                                                  self.city_data[now_city])  # 计算两点距离
            circle_distance += self.distance_between_two_city(self.city_data[now_city],
                                                                      self.city_data[self.pop[i][0]])
            self.old_pop_fitness.append(circle_distance)

    # 选择函数
    def selection(self):
        # 精英保留
        # 1.选择的个体
        union_pop_fitness = self.old_pop_fitness + self.pop_fitness   # 将老的适应度和新的适应度并集

        sort_fitness_num = sorted(range(self.pop_size*2), key=lambda x: union_pop_fitness[x]) # 从小到大排序，返回从小到大排个体的索引号
        choice_individual_num = sort_fitness_num[:self.pop_size]     # 精英保留的个体索引号
        for i in choice_individual_num:
            if i < self.pop_size :
                self.choice_pop.append(self.pop[i])     # 如果该索引小于self.city_size说明是self.pop中的个体
            else:                                       # 否则是self.new_pop中的个体
                self.choice_pop.append(self.new_pop[i-self.pop_size])

    # ------------
    #   停止条件
    # -------------
    def stop_rule(self):  # NG最大迭代数 100~500
        # 满足最大迭代次数时停止
        if self.age == self.num_gen:
            return 0
        else:
            return 1



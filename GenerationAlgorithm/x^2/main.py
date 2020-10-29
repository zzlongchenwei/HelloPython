"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:main.py
"""

# ****************************************************************
# 将设置->工具->python scientific->在工具窗口中显示绘图勾去掉，不然会内存爆炸
# ****************************************************************
from GA import GA
from plot import *



if __name__ == '__main__':
    interval = [-10, 10]  # 区间
    mod = 'min'  # 模式
    func = lambda x: x**2
    # func = lambda x: (x**2)*np.sin(4*x)
    scal = 1
    NG = 150
    pop_size = 30

    # 产生一个种群
    ga = GA(func, mod, scal, interval, NG, pop_size)  # 一个种群实例
    ga.produce_rpop()  # 创建一个实数编码种群

    plot_func(func, ga.pop)
    # print('当前种群', ga.pop)  # 打印该种群
    # print('----' * 10)
    while ga.stop_rule():
        print('========>第%s代开始' % ga.age)
        print('当前种群', ga.pop)
        print('-----' * 10)

        # 交叉
        ga.crossover(op_alph=1)
        print('----' * 10)

        # 变异
        ga.mutation(mod='gauss')
        print('----' * 10)

        # 选择
        ga.pro_fitness()  # 计算适应值
        print('----' * 10)
        ga.rws()  # 轮盘赌选择
        print('----' * 10)

        # 更新种群
        ga.update_pop()
        print('===========>第%s代结束' % ga.age)
        print('------------------'*10)

        ga.age += 1

        # 画图
        # plot_func(func, ga.pop)

    print('迭代%s完成' % ga.age)
    print('最优解:', ga.optimized_value()[1], '最优值:', ga.optimized_value()[0][0])
    plot_func(func, ga.pop, draw=0)






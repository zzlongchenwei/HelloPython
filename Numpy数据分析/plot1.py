"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/22  @author:zzlong  
@file:20201022_plot1.py
"""

import matplotlib.pyplot as plt
import numpy as np

# 以自然数序列作为多项式的系数，使用poly1d函数创建多项式
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
# 使用numpy的linspace函数创建x轴的数值，在-10到10之间产生30个均匀分布的值
x = np.linspace(-10, 10, 30)
# 计算在第一步中创建的多项式的值
y = func(x)
# 调用plot函数，不会立刻显示函数图像
plt.plot(x, y)
# 使用xlable函数添加x轴标签
plt.xlabel('x')
# 使用ylabel函数添加y轴标签
plt.ylabel('y(x)')
# 调用show函数显示函数图像
plt.show()

if __name__ == '__main__':
    pass
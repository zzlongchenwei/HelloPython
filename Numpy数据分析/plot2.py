"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/22  @author:zzlong  
@file:plot2.py
"""
import matplotlib.pyplot as plt
import numpy as np

#
# func = lambda x: x**2
# x = np.linspace(-10, 10)
# y = func(x)
# plt.title('y = x^2')
# plt.xlabel('x')
# plt.ylabel('y')
# #
# plt.plot(x, y)
#
# piontx = np.arange(-10,10)
# pionty = func(piontx)
# plt.scatter(piontx, pionty)

line, = plt.plot([1, 2, 3])
line.set_label('Label via method')
plt.legend()
plt.show()

if __name__ == '__main__':
    pass

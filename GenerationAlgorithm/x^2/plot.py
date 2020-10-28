"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/22  @author:zzlong  
@file:ploy.py
"""
import matplotlib.pyplot as plt
import numpy as np


def plotfunc(func, pointx, draw=1):
    plt.ion()  # 开启interactive mode
    # fig = plt.figure()
    plt.cla()
    x = np.linspace(-10, 10, 1000)
    y = func(x)
    plt.title('func')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y)
    pointy = []
    for i in range(len(pointx)):
        pointy.append(func(pointx[i]))
    plt.scatter(pointx, pointy, s=60 , c='r', marker='.')
    if draw:
        plt.draw()
        plt.pause(0.05)
        # plt.ioff()  # 开启interactive mode
        # plt.close(1)
    else:
        plt.ioff()  # 开启interactive mode
        plt.show()  # 程序会停到这


if __name__ == '__main__':
    func = lambda x: x**2
    # plotfunc(func)

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:tspPlot.py
@time:2020/11/03
"""

import matplotlib.pyplot as plt
from ReadData import *
plt.style.use('seaborn-whitegrid')


def plot_fit(fitness):
    plt.plot(range(len(fitness)), fitness)
    plt.show()


def draw_city(city_data):
    city_data_item = city_data.items()
    for city, coord in city_data_item:
        x = coord[0]
        y = coord[1]
        plt.plot(x, y, marker='s', markersize=6, label=city)
        plt.text(x, y, city, color='b')
        plt.legend()
        plt.draw()
    # plt.show()


def draw_figure(city_data):
    draw_city(city_data)

    def draw_arrow(start, end):  # 起始坐标，终点坐标
        plt.arrow(start[0], start[1], end[0] - start[0], end[1] - start[1], width=0.03, fc='g',
                  length_includes_head=True)
        plt.draw()

    return draw_arrow


def plot_arrow(a_individual):
    for i in range(len(a_individual)):
        if i == len(a_individual) - 1:
            draw_line(city_data[a_individual[i]], city_data[a_individual[0]])
        else:
            draw_line(city_data[a_individual[i]], city_data[a_individual[i + 1]])
    plt.show()


if __name__ == '__main__':
    city_data = read_city_data('city_coordinate.csv')
    draw_line = draw_figure(city_data)
    a_individual = [12, 10, 2, 13, 9, 7, 8, 3, 6, 1, 14, 11, 5, 4]
    plot_arrow(a_individual)

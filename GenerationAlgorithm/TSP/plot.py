#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:plot.py
@time:2020/11/03
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
from ReadData import *



def draw_city(city_data):
    city_data_item = city_data.items()
    for city, coord in city_data_item:
        x = coord[0]
        y = coord[1]
        plt.plot(x, y, marker='s', markersize=4)
        plt.text(x, y, city)
        plt.draw()
    plt.show()

def draw_arrow(current_min, current_path):
    pass

if __name__ == '__main__':
    city_data = read_city_data('city_coordinate.csv')
    draw_city(city_data)

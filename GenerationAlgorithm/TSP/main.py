#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:main.py
@time:2020/10/30
"""

from tspGA import GA

if __name__ == '__main__':
    ga = GA(city_num=14)
    ga.produce_pop()

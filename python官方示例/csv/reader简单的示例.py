#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:reader简单的示例.py
@time:2020/10/30
"""
import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # 一行一行迭代
    # delimiter = ' '以空格为分割标志
    # quotechar='|' 以||包住特殊字符的字段
    print(spamreader)
    for row in spamreader:
        print(', '.join(row))
    csvfile.seek(0)
    for row in spamreader:
        print(row)



#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:writer示例.py
@time:2020/10/30
"""
import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     # 根据`Dialect.delimiter`这个指定 定界符。
#     # 和`Dialect.quotechar`联动，可以换成其他符号，不光是引号
#     # quoting=csv.QUOTE_MINIMAL只为包含特殊字符的字段加上Dialect.quotechar指定的符号
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('test.csv','w', newline='') as cf:
    spamwirter = csv.writer(cf)
    spamwirter.writerow([66]*10 + ['a,b'])
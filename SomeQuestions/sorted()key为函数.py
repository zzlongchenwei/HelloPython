"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/04  @author:zzlong  
@file:sorted()key为函数.py
"""

lis = [1, 2, 3, 0, 1, 9, 8]
print(sorted(range(len(lis)), key=lambda k: lis[k]))
# range(len(lis)) = [0, 1, 2, 3, 4, 5, 6]
# 0 :lis[0] = 1
# 1:lis[1] = 2
# 2:lis[2] = 3
# 3:lis[3] = 0
# 4:lis[4] = 1
# 5:lis[5] = 9
# 6:lis[6] = 8

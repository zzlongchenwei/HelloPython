#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:精英保留测试.py
@time:2020/11/02
"""
# 问题:改错了，应该再算一次原种群的适应度

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
sort_num = sorted(range(3*2), key=lambda x:l3[x])
print(sort_num)

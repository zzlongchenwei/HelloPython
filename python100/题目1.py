"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/04  @author:zzlong  
@file:题目1.py
"""

# 程序1
# 题目：有1，2，3，4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少?
numlist = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                numlist.append(str(i)+str(j)+str(k))
print(numlist)


def comNumber(num='', figure=3):
    l = ['1', '2', '3', '4']
    for i in l:
        if i not in num:
            if len(num) == figure-1 :
                yield i
            else:
                for j in comNumber(num+i):
                    yield i+j


print(list(comNumber()))

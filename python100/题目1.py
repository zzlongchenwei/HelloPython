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


def NumToCh(startnum,endnum):
    # 将数字列表转为字符串列表，
    # startnum为列表起始数字
    # endnum为终止数字
    ch = []
    for i in range(startnum, endnum+1):
        ch.append(str(i))
    return ch


def comNumber(startnum=1,endnum=4,figure=3):
    # startnum起始数字，endnum终止数字，figure几位数字组合
    l = NumToCh(startnum,endnum)

    def nextNumber(chnum=''):
        # 递归部分
        for i in l:
            if i not in chnum:
                # 如果该数字不在chnum中则继续
                if len(chnum) == figure-1 :
                    # 如果是最后一个数字，就生成该数字
                    yield i
                else:
                    for j in nextNumber(chnum+i):
                        # 递归数字
                        yield i+j
    return nextNumber


print(list(comNumber()()))

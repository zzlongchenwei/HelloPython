#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19


# 通用做法---迭代
data = [1, 5, -3, -2, 6, 0, 9]
res = []
for x in data:
    if x >= 0:
        res.append(x)
print("res:", res)

# --------------------------------------------- #

# filter函数
from random import randint

data = [randint(-10, 10) for _ in range(10)]
print("data:", data)
# lambda迭代,大于零返回布尔值
tempdata2 = filter(lambda x: x >= 0, data)
data2 = list(tempdata2)
print("data2:", data2)

# --------------------------------------------- #

# 列表解析  (速度更快)
data3 = [x for x in data if x >= 0]
print("data3:", data3)

# --------------------------------------------- #

#
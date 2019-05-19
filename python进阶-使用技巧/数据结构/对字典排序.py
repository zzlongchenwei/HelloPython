#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19

from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}
print(d)

print(sorted(d))

iter(d)

print(list(iter(d)))

# 元组比较先比较第一个，再比较第二个
# (97,'a')<(69,'b')

# -----------------------------  #
# zip函数
d.keys()
d.values()
zip(d.values(), d.keys())

z = sorted(zip(d.values(), d.keys()))
print(z)

# --------------------------------- #
# 使用sorted()函数的key
d = {x: randint(60, 100) for x in 'xyzabc'}
d.items()
z = sorted(d.items(), key=lambda x: x[1])
print(z)

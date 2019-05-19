#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19
from random import randint

data = [randint(-10, 10) for _ in range(10)]
print('列表data:',data)

s = set(data)
print("集合set:",s)

# 集合解析
s2 = {x for x in s if x % 3 ==0}
print("能被三整除:",s2)

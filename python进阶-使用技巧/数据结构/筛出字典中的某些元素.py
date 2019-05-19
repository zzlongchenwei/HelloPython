#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19

from random import randint

d = {x: randint(60,100) for x in range(1,21)}
print("字典：",d)

# 字典解析
bigger90 = {k:v for k,v in d.items() if v>90}
print("bigger90:",bigger90)


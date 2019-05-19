#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19

from collections import Counter
import re

txt = open('G:\\Hello-Python\\小练习\\test.txt').read()
c3 = Counter(re.split('\W', txt))
print(c3)
c3.most_common(5)
print(c3.most_common(5))

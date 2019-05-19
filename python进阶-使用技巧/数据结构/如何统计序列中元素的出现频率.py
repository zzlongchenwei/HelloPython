#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19

from random import randint

# 生成随机列表
data = [randint(2, 20) for _ in range(20)]
print(data)
# 建一个以data为键的字典
c = dict.fromkeys(data, 0)
print(c)
# 遍历键 ，在data中出现一次+1
for x in data:
    c[x] += 1
print(c)
# items()方法将字典的元素 转化为了元组，而这里key参数对应的lambda表达式的意思则是选
# 取元组中的第二个元素作为比较参数（如果写作key=lambda item:item[0]的话则是选取第一
# 个元素作为比较对象，也就是key值作为比较对象。
c1 = sorted(c.items(), key=lambda x: x[1], reverse=True)
print(c1)
# 注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组
c2 = dict(c1)
print(c2)

# ------------------------------------------------------------------ #

# 使用Counter函数
from collections import Counter
c3 = Counter(data)
# c3.most_common(3)统计出频率最高的三个数
print(c3.most_common(3))


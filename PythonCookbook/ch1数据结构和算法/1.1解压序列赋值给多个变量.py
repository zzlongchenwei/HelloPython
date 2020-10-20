"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/09  @author:zzlong  
@file:1.1解压序列赋值给多个变量.py
"""

# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。
# 唯一的前提就是变量的数量必须跟序列元素的数量是一样的
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2020, 10, 9)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)


# 如果变量个数和序列元素的个数不匹配，会产生一个异常
p = (4, 5)
# x, y, z = p
# (<class 'ValueError'>, ValueError('not enough values to unpack (expected 3, got 2)'), <traceback object at 0x0000020B8897B040>)


# 这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
# 包括字符串，文件类型，迭代器和生成器
s = 'hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)


# 只想解压一部分，使用任意变量名去占位，到时候丢掉这些变量就行
data = ['ACME', 50, 91.1, (2020, 10, 9)]
_, shares, price, _ = data
print(shares)
print(price)
# 你必须保证你选用的那些占位变量名在其他地方没被使用到

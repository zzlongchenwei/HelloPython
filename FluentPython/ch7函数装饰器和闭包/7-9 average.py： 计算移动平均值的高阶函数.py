# -*- coding: utf-8 -*-

# @File    : 7-9 average.py： 计算移动平均值的高阶函数.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-
def make_averager():
    series = []     # 没有给series赋值，所以不是局部变量，调用series.append并传给sum和len，利用了列表是可变的对象

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return average


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__code__.co_varnames) # __code__编译后的函数的定义体
print(avg.__code__.co_freevars)
print(avg.__closure__)  # cell对象
print(avg.__closure__[0].cell_contents)  # cell_contents属性，保存着真正的值



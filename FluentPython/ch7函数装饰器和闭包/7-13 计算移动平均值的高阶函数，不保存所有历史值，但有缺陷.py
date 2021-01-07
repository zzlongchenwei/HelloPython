# -*- coding: utf-8 -*-

# @File    : 7-13 计算移动平均值的高阶函数，不保存所有历史值，但有缺陷.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-

"""问题：count，total为什么为局部变量了？"""
def make_averager():
    count = 0  # 此时给count赋了值，会将count变为局部变量
    total = 0  # 同上

    def averager(new_value):
        count += 1  # 对数字、字符串、元组等不可变类型来说，只能读取，不能更新
        total += new_value  # 对数字、字符串、元组等不可变类型来说，只能读取，不能更新
        return total / count  # 对数字、字符串、元组等不可变类型来说，只能读取，不能更新

    return averager



"""解决"""
def make_averager_new():
    count = 0  # 此时给count赋了值，会将count变为局部变量
    total = 0  # 同上

    def averager(new_value):
        nonlocal count, total  # nonlocal
        count += 1
        total += new_value
        return total / count

    return averager

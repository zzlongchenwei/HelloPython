# !/usr/bin/python
# -*- coding: UTF-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# @author:zzlong  @file:递归生成器.py
# @time:2020/09/22


# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
def flatten(nested):
    try:
        for sublist in nested:                     # 遍历所有子列表
            # print(sublist)
            for element in flatten(sublist):       # 再对子列表调用flatten,再使用for循环生成展开后所有元素。
                # print("分支1",element)
                yield element                       # 生成该元素
    except TypeError:                               # 如果该元素为数字就会产生typeError
        # print("分支2",nested)
        yield nested                            # 就生成该数字


nested = [[[1], 2], 3, 4, [5, [6, 7]], 8]
for num in flatten(nested):
    print(num)

print(list(flatten(nested)))


def flatten(nested):
    try:
         # 不迭代类似于字符串的对象：
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
             for element in flatten(sublist):
                yield element
    except TypeError:
         yield nested
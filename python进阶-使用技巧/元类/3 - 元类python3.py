#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26

def upper_attr(future_class_name, future_class_parant, future_class_attr):
    # 便利属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value


    # 调用type来创建一个类
    return type(future_class_name, future_class_parant, newAttr)

# 与python2不同
class Foo(object, metaclass = upper_attr):
    bar = 'bip'

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f = Foo()
print(f.BAR)

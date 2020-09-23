#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/6/5

# __init__  构造初始化函数
# __new__   生成实例所需属性
# __class__ 实例所在的类
# __repr__  实例字符串表示，准确性
# __str__   实例字符串表示，可读性
# __del__   析构
# __dict__  实例自定义属性
# __doc__   类文档，子类不继承
# __getattribute__ 属性访问拦截器
# __base__  类的所有父类构成元素


class Itcast(object):
    def __init__(self, subject1):  # obj --> "subject1"
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # 属性访问时拦截器，打log
    def __getattribute__(self, obj):
        print("===1>%s" % obj)
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:  # 测试时注释掉这2行，将找不到subject
            temp = object.__getattribute__(self, obj)    # obj --> "subject2"
            print("===2>%s" % str(temp))
            return temp

    def show(self):
        print('this is Itcast')


s = Itcast("python")             # 传入"python"是因为 __init__() required positional argument: 'subject1'
print(s.subject1)
print(s.subject2)

s.show()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19


# 定义类似于其他语言的枚举类型
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
NAME, AGE, SEX, EMAIL = range(4)

student = ('Jim', 16, 'male', 'jim8872@gmail.com')

# name
print = (student[NAME])

# age
if student[AGE] >= 18:
    pass
    # ...

# sex
if student[SEX] == 'male':
    pass
    #  ...

# 使用collections.namedtuple替代内置tuple
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jim', 16, 'male', 'jim8872@gmail.com')
s.name
#'Jim'
s.age
#16
s.sex
#'male'
s.email
#'jim8872@gmail.com'
isinstance(s,tuple)
#True
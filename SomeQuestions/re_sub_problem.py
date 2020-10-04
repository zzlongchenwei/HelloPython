"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/09/28  @author:zzlong  
@file:re_sub_problem.py
"""

import re


def replace_num(st):
    print(st)
    numDict = {'0': '〇', '1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}
    print(st.group())
    return numDict[st.group()]


my_str = '2018年6月7号'
a = re.sub(r'(\d)', replace_num, my_str)
print(a)  # 每次匹配一个数字，执行函数，获取替换后的值


m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
print(m.group(0))
print(m.group(1))
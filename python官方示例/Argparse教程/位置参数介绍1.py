"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/13  @author:zzlong  
@file:位置参数介绍.py
"""

import argparse

# Argument实参
parser = argparse.ArgumentParser()
parser.add_argument("echo")
# add_argument() 方法，该方法用于指定程序能够接受哪些命令行选项
args = parser.parse_args()
# The parse_args() method actually returns some data from the options specified, in this case, echo.
# parse_args()方法实际上从指定的选项(在本例中为echo)返回一些数据。
print(args.echo)
# 这一变量是 argparse 免费施放的某种 “魔法”（即是说，不需要指定哪个变量是存储哪个值的）。
# 你也可以注意到，这一名称与传递给方法的字符串参数一致，都是 echo。

# 终端运行结果：
# F:\WorkSpace\Hello-Python\python官方示例\Argparse教程>python 位置参数介绍.py foo
# foo

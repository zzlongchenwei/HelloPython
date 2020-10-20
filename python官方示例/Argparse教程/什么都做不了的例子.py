"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/13  @author:zzlong  
@file:例子1.py
"""

import argparse


parser = argparse.ArgumentParser()
parser.parse_args()

# --help 选项，也可缩写为 -h，是唯一一个可以直接使用的选项（即不需要指定该选项的内容）

# 终端运行结果：
# F:\WorkSpace\Hello-Python\python官方示例\Argparse教程>python 什么都做不了的例子.py -h
# usage: 什么都做不了的例子.py [-h]
#
# optional arguments:
#   -h, --help  show this help message and exit

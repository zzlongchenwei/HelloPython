"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/13  @author:zzlong  
@file:位置参数介绍3.py
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)

# 进展不太顺利。那是因为 argparse 会把我们传递给它的选项视作为字符串，除非我们告诉它别这样。

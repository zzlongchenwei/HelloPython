"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/13  @author:zzlong  
@file:位置参数介绍2.py
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
# parse_args()方法实际上从指定的选项(在本例中为echo)返回一些数据。
print(args.echo)


# F:\WorkSpace\Hello-Python\python官方示例\Argparse教程>python 位置参数介绍2.py -h
# usage: 位置参数介绍2.py [-h] echo
#
# positional arguments:
#   echo        echo the string you use here
#
# optional arguments:
#   -h, --help  show this help message and exit

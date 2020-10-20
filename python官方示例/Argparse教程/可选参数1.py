"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/13  @author:zzlong  
@file:可选参数.py
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")

# 这一程序被设计为当指定 - -verbosity选项时显示某些东西，否则不显示。
# 不添加这一选项时程序没有提示任何错误而退出，表明这一选项确实是可选的。注意，如果一个可选参数没有被使用时，相关变量被赋值为
# None，在此例中是args.verbosity，这也就是为什么它在 if 语句中被当作逻辑假。帮助信息有点不同。
# 使用 - -verbosity选项时，必须指定一个值，但可以是任何值。

# $ python3 prog.py --verbosity 1
# verbosity turned on
# $ python3 prog.py --verbosity
# usage: prog.py [-h] [--verbosity VERBOSITY]
# prog.py: error: argument --verbosity: expected one argument
# $ python3 prog.py --help
# usage: prog.py [-h] [--verbosity VERBOSITY]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --verbosity VERBOSITY
#                         increase output verbosity

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")

# 现在，这一选项更多地是一个标志，而非需要接受一个值的什么东西。我们甚至改变了选项的名字来符合这一思路。
# 注意我们现在指定了一个新的关键词 action，并赋值为 "store_true"。这意味着，当这一选项存在时，为 args.verbose 赋值为 True。
# 没有指定时则隐含地赋值为 False。
# 当你为其指定一个值时，它会报错，符合作为标志的真正的精神。
# 留意不同的帮助文字。

# $ python3 prog.py --verbose
# verbosity turned on
# $ python3 prog.py --verbose 1
# usage: prog.py [-h] [--verbose]
# prog.py: error: unrecognized arguments: 1
# $ python3 prog.py --help
# usage: prog.py [-h] [--verbose]
#
# optional arguments:
#   -h, --help  show this help message and exit
#   --verbose   increase output verbosity

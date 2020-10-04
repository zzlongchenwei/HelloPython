"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/09/28  @author:zzlong  
@file:util.py
"""


def lines(file):
    for line in file: yield line        # 迭代文件的每一行，并生成该行
    yield '\n'                          # 最后一行生成一个空行


def blocks(file):
    block = []
    for line in lines(file):            # 迭代生成器
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()        # 使用''将block合并，并去掉两边的空白
            block = []

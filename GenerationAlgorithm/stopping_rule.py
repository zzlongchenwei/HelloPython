"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:stopping_rule.py
"""


class StoppingRule:
    """
    停止准则
    """
    def __init__(self, num_max_gen):
        # age 迭代数
        self.age = 0
        # 最大迭代次数
        self.NG = num_max_gen

    def stop_rule(self):
        # 满足最大迭代次数时停止
        if self.age == self.NG:
            return

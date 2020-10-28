"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/19  @author:zzlong  
@file:stopping_rule.py
"""


def stop_rule(age, NG=100):  # NG最大迭代数 100~500
        # 满足最大迭代次数时停止
        if age == NG:
            return 0
        else:
            return 1

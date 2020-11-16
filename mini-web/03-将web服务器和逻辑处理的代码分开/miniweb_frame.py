#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:mini_frame.py
@time:2020/11/15
"""
import time


def login():
    return "---login----welcome to our website ...time: %s" % time.ctime()

def register():
    return "---register---...time: %s" % time.ctime()

def profile():
    return "---profile---time: %s" % time.ctime()

def application(file_name):
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "not found your page."

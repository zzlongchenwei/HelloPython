#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:mini_frame.py
@time:2020/11/16
"""

def application(environ, start_response):
    start_response('200 OK', [('Connect-Type', 'text/html;charset=utf-8')])
    return 'Hello World! 中文乱码'

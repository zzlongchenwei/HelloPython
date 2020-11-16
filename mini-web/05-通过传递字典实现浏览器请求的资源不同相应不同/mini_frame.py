#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:mini_frame.py
@time:2020/11/15
"""

def index():
    pass
    return "这是主页"
def login():
    pass
    return "这是登录页"

def application(environ, start_response):
    start_response('200 OK', [('Connect-Type', 'text/html;charset=gbk')])

    file_name = environ['PATH_INFO']
    # file_name = '/index.py'
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello World! 中文乱码'

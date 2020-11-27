#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:mini_frame.py
@time:2020/11/22
"""
import re

# 装饰器已经提前加载了，所以可以写在前面
URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.html"] = index
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route("/index.html")
def index():
    with open("./template/index.html") as f:
        content = f.read()

    my_stock_info = "index"
    content = re.sub(r"haha", my_stock_info, content)

    return content


@route("/center.html")
def center():
    with open("./template/center.html") as f:
        content = f.read()

    my_stock_info = "center"
    content = re.sub(r"haha", my_stock_info, content)

    return content


# URL_FUNC_DICT = {
#     '/index.html': index,
#     '/center.html': center
# }


def application(environ, start_response):
    start_response('200 OK', [('Connect-Type', 'text/html;charset=utf-8')])

    file_name = environ['PATH_INFO']
    # file_name = '/index.py'
    # if file_name == '/index.py':
    #     return index()
    # elif file_name == '/login.py':
    #     return login()
    # else:
    #     return 'Hello World! 中文乱码'
    # try:
    func = URL_FUNC_DICT[file_name]
    return func()
        # return URL_FUNC_DICT[file_name]()
    # except Exception as err:
    #     return "产生了异常：%s" % str(err)

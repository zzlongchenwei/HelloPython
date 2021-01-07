# -*- coding: utf-8 -*-

# @File    : 7-21 singledispatch 创建一个自定义的.py
# @Date    : 2021-01-07
# @Author  : chenwei    -剑衣沉沉晚霞归，酒杖津津神仙来-
from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch # 使用singledispatch标记处理object类型的基函数
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)  # 各个专门函数使用 @«base_function».register(«type») 装饰
def _(text):
    content = html.escape(text).replace('\n','<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.regsiter(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n</nl>' + inner + '</li>\n</ul>'
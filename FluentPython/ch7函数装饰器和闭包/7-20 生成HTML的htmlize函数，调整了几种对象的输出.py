# -*- coding: utf-8 -*-

# @File    : 7-20 生成HTML的htmlize函数，调整了几种对象的输出.py
# @Date    : 2021-01-07
# @Author  : chenwei    -剑衣沉沉晚霞归，酒杖津津神仙来-
import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)



print(htmlize({1,2,3}))
print(htmlize(abs)) # 函数
print(htmlize('Heimlich & Co.\n- a game')) # 字符串
print(htmlize(42)) # 数字
print(htmlize(['alpha', 66, {3, 2, 1}]))



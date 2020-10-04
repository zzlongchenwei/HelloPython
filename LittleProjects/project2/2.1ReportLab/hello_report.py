"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/03  @author:zzlong  
@file:hello_report.py
"""

from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello, world!', textAnchor='middle')
# 构造函数String的主要参数包括x坐标和y坐标以及文本。
# 参数textAnchor，它指定要将字符串的哪部分放在坐标指定的位置
d.add(s)

renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')

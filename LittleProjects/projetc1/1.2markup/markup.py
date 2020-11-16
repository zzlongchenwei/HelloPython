"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/09/30  @author:zzlong  
@file:markup.py
"""

import sys, re
from handlers import *
from util import *
from rules import *


class Parser:
    """
    Parser读取文本文件，应用规则并控制处理程序
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)     # 将filter函数的引用添加到fileters列表中

    def parse(self, file):
        # 用一个匹配法和一个规则对一种文本进行处理，如果是FALSE则继续调用其他匹配法和规则处理，否则就BREAK处理完毕。
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler) # 使用filters列表中的各类filter函数对block进行匹配替换
            for rule in self.rules:                # 原版缩进错误，导致break后进入上一个循环进来后再运行一次，一共有三个匹配所以会重复三次
                if rule.condition(block):
                    if rule.action(block, self.handler): break  # 不想尝试其他规则，返回True，以结束对当前文本块的处理
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    在构造函数中添加规则和过滤器的Parser子类
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(tcp_server_socket'\*(.+?)\*', 'emphasis')
        self.addFilter(tcp_server_socket'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(tcp_server_socket'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)

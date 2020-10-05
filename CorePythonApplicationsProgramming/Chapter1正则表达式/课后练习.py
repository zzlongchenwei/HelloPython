"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/04  @author:zzlong  
@file:1-1.py
"""

# 1-1识别后续的字符串： “bat”、“bit”、“but”、“hat”、“hit”或者“hut”。
import re
patt = re.compile(r'b[aiu]t|h[aiu]t')
s = 'batbitbuthathithut'
print(re.findall(patt, s))


# 1-2匹配由单个空格分隔的任意单词对，也就是姓和名
patt = re.compile(r'[A-Z][a-z]*\s[A-Za-z]+')
s = "Zhao Long, Zhang San, Li TieZhu, qitaren, I'm Li Si ."
print(re.findall(patt, s))


# 1-3匹配由单个逗号和单个空白符分隔的任何单词和单个字母，如姓氏的首字母。
patt = re.compile(r'[A-Za-z]+,\s[A-Za-z]')
s = "Zhao Long, Zhang San, Li TieZhu, qitaren, I'm Li Si ."
print(re.findall(patt, s))


# 1-4匹配所有有效 Python 标识符的集合
patt = re.compile(r'[a-zA-Z_]\w+')

# 1-5根据读者当地的格式，匹配街道地址（使你的正则表达式足够通用，来匹配任意数
# 量的街道单词，包括类型名称）。例如，美国街道地址使用如下格式： 1180 Bordeaux
# Drive。使你的正则表达式足够灵活，以支持多单词的街道名称，如 3120 De la Cruz
# Boulevard
pat = re.compile(r'\d+[\sa-zA-Z]+')
s = '1180 Bordeaux Drive 3120 De la Cruz Boulevard'
print(re.findall(pat, s))

# 匹配以“www”起始且以“.com”结尾的简单 Web 域名；例如， www://www. yahoo.com/。
# 选做题： 你的正则表达式也可以支持其他高级域名，如.edu、 .net 等（例如，
# http://www.foothill.edu）
patt = re.compile(r'www[\S]+\.com|www[\S]+\.net|www[\S]+\.edu')
s = 'www.foothill.edu, www://www.yahoo.com'
print(re.findall(patt, s))
# ^Subject: hi$ 任何由单独的字符串 Subject: hi 构成的字符串
# 如果^ 和$连用表示匹配由这俩符号夹在中间的字符串
# ^ $  /A /Z

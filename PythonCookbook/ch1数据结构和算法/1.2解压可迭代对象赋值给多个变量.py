"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/09  @author:zzlong  
@file:1.2解压可迭代对象赋值给多个变量.py
"""

# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError
# python星号表达式可以解决这个问题


# def drop_first_last(grades):
#     """
#     比如，你在学习一门课程，在学期末的时候，你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
#     如果只有四个分数，你可能就直接去简单的手动赋值，但如果有 24 个呢？这时候星号表达式就派上用场了：
#     """
#     first, *middle, last = grades
#     return avg(middle)

# 假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_nambers = record
print(name)
print(email)
print(phone_nambers)  # phone_numbers 变量永远都是列表类型,包括 0 个

# 星号表达式也能用在列表的开始部分。
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

# 扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的。

# 值得注意的是，星号表达式在迭代元素为可变长元组的序列时是很有用的。
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# 你想解压一些元素后丢弃它们，你不能简单就使用 * ，但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ ignore）
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

# 星号解压语法跟列表处理有许多相似之处
items = [1, 10, 7, 4, 5, 9]
# head, *tail = items
# print(head)
# print(tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head  # 如果tail不为空就返回head+*tial否则只返回head


print(sum(items))


"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/09  @author:zzlong  
@file:1.3保留最后N个元素.py
"""

# 保留有限历史记录正是 collections.deque 大显身手的时候。
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
# deque([iterable[, maxlen]]) –> deque object
# A list-like sequence optimized for data accesses near its endpoints.
# 为接近其端点的数据访问而优化的类列表序列。
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
# 迭代文件内容：迭代文件内容的方法很多，其中最常见的是迭代文本文件中的行，这可
# 通过简单地对文件本身进行迭代来做到。还有其他与较旧Python版本兼容的方法，如使用
# readlines。

# example use on a file
if __name__ == '__main__':
    with open(tcp_server_socket'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
                print(line, end='')
                print('-' * 20)


# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
# 当新的元素加入并且这个队列已满的时候，最老的元素会自动被移除掉。
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

# 更一般的， deque 类可以被用在任何你只需要一个简单队列数据结构的场合。如果
# 你不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添
# 加和弹出元素的操作。
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
# 在队列两端插入或删除元素时间复杂度都是 O(1) ，而在列表的开头插入或删除元素的时间复杂度为 O(N)

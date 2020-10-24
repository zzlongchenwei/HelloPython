"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:12..py
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0

    def push(self, item, priority):
        heapq.heappush(self.__queue, (-priority, self.__index, item))
        # 第一个参数：添加进的目标序列
        # 第二个参数：将一个元组作为整体添加进序列，目的是为了方便比较
        # 在priority相等的情况下，比较_index
        # priority为负数使得添加时按照优先级从大到小排序，因为堆排序的序列的第一个元素永远是最小的
        self.__index += 1

    def pop(self):
        # 返回按照-priority 和 _index 排序后的第一个元素(是一个元组)的最后一个元素(item)
        return heapq.heappop(self.__queue)[-1]


q = PriorityQueue()
q.push("bar", 2)
q.push("foo", 1)
q.push("gork", 3)
q.push("new", 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

"""
gork  # 优先级最高
bar   # 优先级第二
foo   # 优先级与new相同，比较index，因为先加入，index比new小，所以排在前面
new
"""

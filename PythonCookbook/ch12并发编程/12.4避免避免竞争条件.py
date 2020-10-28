"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/25  @author:zzlong  
@file:12.4避免避免竞争条件.py
"""
import threading
# 12.4给临界区加锁以避免竞争条件.py的变种


class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        '''
        Increment the counter with locking
        '''
        self._value_lock.acquire()  # 显式的获得锁
        self._value += delta
        self._value_lock.release()  # 显式的解锁

    def decr(self, delta=1):
        '''
        Decrement the counter with locking
        '''
        self._value_lock.acquire()  # 显式的获得锁
        self._value -= delta
        self._value_lock.release()  # 显式的解锁

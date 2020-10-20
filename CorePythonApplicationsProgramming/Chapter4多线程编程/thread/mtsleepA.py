"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/16  @author:zzlong  
@file:mtsleepA.py
"""

import _thread
from time import sleep, ctime


def loop0():
    print('start loop0 at:', ctime())
    sleep(4)
    print('loop0 done at:', ctime())


def loop1():
    print('start loop1 at:', ctime())
    sleep(2)
    print('loop1 done at:', ctime())


def main():
    print('starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()


# starting at: Fri Oct 16 22:07:44 2020
# start loop0 at: Fri Oct 16 22:07:44 2020   -------+ loop0和loop1 一起开始
# start loop1 at: Fri Oct 16 22:07:44 2020   -------+
# loop1 done at: Fri Oct 16 22:07:46 2020    -------> loop1 sleep了两秒
# loop0 done at: Fri Oct 16 22:07:48 2020    -------> loop0 sleep了四秒
# all DONE at: Fri Oct 16 22:07:50 2020      -------> main sleep了六秒

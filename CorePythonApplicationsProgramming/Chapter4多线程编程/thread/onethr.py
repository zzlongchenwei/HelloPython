"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/16  @author:zzlong  
@file:onethr.py
"""

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
    loop0()
    loop1()
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()


# starting at: Fri Oct 16 22:08:35 2020
# start loop0 at: Fri Oct 16 22:08:35 2020
# loop0 done at: Fri Oct 16 22:08:39 2020
# start loop1 at: Fri Oct 16 22:08:39 2020
# loop1 done at: Fri Oct 16 22:08:41 2020
# all DONE at: Fri Oct 16 22:08:41 2020

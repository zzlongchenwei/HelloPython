#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:flags_threadpool.py
@time:2020/11/23
"""
from concurrent import futures
from flags import save_flag, get_flag, show, main

MAX_WORKER = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image,cc.lower()+'.gif')
    return cc


def download_many(cc_List):
    workers = min(MAX_WORKER,len(cc_List))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one,sorted(cc_List))

    return len(list(res))


if __name__ == '__main__':
    main(download_many)

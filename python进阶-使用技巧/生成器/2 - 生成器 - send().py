#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26

def test():
    i = 0
    while i<5:
        temp = yield i  # 第一次运行程序会停止在等号右边，
                        # 再次运行才会执行右边的赋值，此时等号右边没有值，所以会打印None
        print(temp)
        i+=1

t = test()

t.__next__()
# 可以让生成器再往下走一步
t.send("haha")          # 等于把“haha”给了temp
# 注意：
# 第一次不能用send("hh")传值，但是第一次的时候可以用t.send(None)
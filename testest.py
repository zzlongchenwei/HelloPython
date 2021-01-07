#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:testest.py
@time:2020/11/23
"""
# import zfec
import numpy as np
# FORMAT_FORMAT = "%%s.%%0%dd_%%0%dd%%s"
# m=3
# mlen = len(str(m))
# format = FORMAT_FORMAT % (mlen, mlen,)
# print(format)
# prefix = 'abc'
# shnum = 1
# suffix = '.fec'
# print(format % (prefix, shnum, m, suffix,))
#
#
# tmat = np.mat([1,0,0,0,
#                 0,1,0,0,
#                 1,2,3,4,
#                3,4,1,2])
# print(np.invert(tmat))
#
# l = "5.+How+much+is+the+potential+income+from+your+business?+Howmuch+money+do+you+expect+to+earn+in+the+first+three+years?+6.+Do+you+have+enough+money+to+start+your+business,+or+will+youhave+to+borrow+money?+Who+might+lend+you+this+money?+7.+What+do+you+want+to+achieve+in+your+first+year?+8.+What+problems+do+you+predict+in+the+first+year?+What+action+canyou+take+to+solve+or+prevent+these+problems?"
# s = l.replace('+', ' ')
# print(s)

B = np.mat([[-1j,2,3],
               [1,0,1j]])

BHB = np.dot(B.H,B)
print(BHB)
print(B.H*B)
# BHB = np.mat([[2,0,0],
#                [0,1,0],
#                   [0,0,3]])
print(np.linalg.eigvals(BHB))
print(np.linalg.norm(BHB))

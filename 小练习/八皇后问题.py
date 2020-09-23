"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
@author:zzlong
@file:八皇后问题.py
@time:2020/09/22
"""


# 如果下一个皇后与当前皇后的x坐标相同或在同一条对角线上，将发生冲突，因此返回True；如果没有发生冲突，就返回False。
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            # 如果下一个皇后的水平距离为0，或者与他们的垂直距离相等（位于对角线上）就返回真
            return True
    return False

# 基线条件
# 这段代码的意思是，如果只剩下最后一个皇后没有放好，就遍历所有可能的位置，并返回那些不会引发冲突的位置。
# def queens(num, state):
#     if len(state) == num - 1:
#         for pos in range(num):
#             if not conflict(state, pos):
#                 yield pos

# print(list(queens(4, (1, 3, 0))))


# 递归条件
def queens(num=8, state=()):
    for pos in range(num):              # 遍历位置
        if not conflict(state, pos):    # 如果不冲突
            if len(state) == num-1:     # 如果是最后一个皇后
                print("分支1",pos)
                yield (pos,)            # 生成位置
            else:
                for result in queens(num, state + (pos,)):    # 不是最后一个皇后，则递归
                    print("分支2","pos",pos,"result",result)
                    yield (pos,) + result


print(list(queens(4)))
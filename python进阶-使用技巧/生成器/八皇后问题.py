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
    for pos in range(num):              # 遍历所有位置 从0 开始从 num-1结束
        if not conflict(state, pos):    # 如果下一个皇后不冲突
            if len(state) == num-1:     # 是最后一个皇后
                print("分支1",pos)
                yield (pos,)            # 生成位置
            else:
                for result in queens(num, state + (pos,)):    # 不是最后一个皇后，则递归
                    print("分支2","pos",pos,"result",result)
                    yield (pos,) + result

# 他先递归到最后一个，再往回逐层返回来，所以调试运行结果是，分支 1 2，分支2 0，分支2 3，分支2 1，
# 递归最后一个就是len(state)==num-1,
# 生成器停止并返回该位置元组，返回到上一层的递归for result in queens 这个queens就是上一层的，
# 然后继续运行下面的yield，完了再返回，直到返回到第一个。

print(list(queens(4)))
# pos = nextX 下一个皇后的横坐标
# queens第一次运行，num=4的话，pos从0~3遍历
# 1===>     state = () , pos = 0 , 进入conflict()判定，for i in range(0)不会运行，返回False，不冲突
# 1===>     判定长度 len(state) = 0 != 3 ，进入else中 for result in queens(4, () + (0,))，递归进queens中，
# 1.1===>   运行queens(4, (0,) ) ，pos从0~3遍历，
# 1.1===>   state(0,)， pos = 0 ， 进入conflict()判断是否冲突，for i in range(1)， state[0] = 0 -0  = 0 ,冲突。
# 1.1===>   停止运行1.1，递归结束，
# 2===>     state = () , pos = 1 ，进入conflict()判定是否冲突，for i in range(0)不会运行，返回False，不冲突
# 2===>     判定长度 len(state) = 0 != 3 ，进入else中 for result in queens(4, () + (1,))，递归进queens中，
# 2.1===>   运行queens(4, (1,) ) ，pos从0~3遍历，
# 2.1===>   state(1,)， pos = 0 ， 判断是否冲突，nextY = len(sate) = 1 ,
#                                 for i in range(1)  ==>  [0]， state[0] = 1 -0  = 1 in (nextY=1 - 0=1),冲突。
# 2.1===>    停止运行2.1，结束此次递归。
# 3===>     state = () , pos = 2 ，进入conflict()判定，for i in range(0)不会运行，返回False，不冲突
# 3===>     判定长度 len(state) = 0 != 3 ，进入else中 for result in queens(4, () + (2,))，递归进queens中，
# 3.1===>   state = (2,) , pos = 0 ,断是否冲突，nextY = len(sate) = 1 ,for i in range(1)  ==>  [0]
#                                       state[0] = 2 -0  = 2 不在 (0 ，nextY=1 - 0=1)中,不冲突。
# 3.1===>    判定长度 len(state) = 1 != 3 ，进入else中 for result in queens(4, (2,) + (0,))，递归进queens中，
# 3.1.1===>   state = (2,0,),pos = 0 ,断是否冲突，nextY = len(sate) = 2 ,for i in range(2)  ==>  [0,1]
#                                       state[0] = 2 -0  = 2 在 (0 ，nextY=2 - 0=2)中,冲突。
#                                       state[1] = 2 -1  = 1 在 (0 ，nextY=2 - 1=1)中,冲突。
# 3.1.1===>  停止运行3.1.1 ，结束此次递归。


def crossover():  # pc为交叉概率 0.4~0.9
    """
    Order Crossover顺序交叉
    a. 选取切点X,Y
    b. 交换中间部分
    c. 从 第二个切点Y 后第一个基因起列出原顺序，去掉已有基因
    d. 从 第二个切点Y 后第一个位置起，将获得无重复顺序填入
    """
    parent = [[7, 2, 4, 1, 12, 5, 11, 8, 10, 9, 3, 13, 6, 14], [8, 13, 6, 4, 14, 3, 12, 10, 2, 1, 9, 7, 11, 5]]  # 从pop中选出两个父代
    print('原父代       ','p1:',parent[0],'p2:',parent[1])

    # a.选取切点X,Y
    X = 14 // 3
    Y = -X

    # c. 从 第二个切点Y 后第一个基因起列出原顺序，去掉已有基因
    # 列出原顺序
    sequence0 = parent[0][Y:] + parent[0][:X] + parent[0][X:Y]
    sequence1 = parent[1][Y:] + parent[1][:X] + parent[1][X:Y]
    print('列出原顺序    ',"p1:",sequence0,"p2:",sequence1)

    # b. 交换中间部分
    parent[0][X:Y], parent[1][X:Y] = parent[1][X:Y], parent[0][X:Y]
    print('交换中间部分  ',"p1:",parent[0][X:Y],"p2:",parent[1][X:Y])
    print("交换后       ","p1:",parent[0],"p2:",parent[1])

    # c. 从 第二个切点Y 后第一个基因起列出原顺序，去掉已有基因
    # # 列出原顺序
    # sequence0 = parent[0][Y:] + parent[0][:X] + parent[0][X:Y]
    # sequence1 = parent[1][Y:] + parent[1][:X] + parent[1][X:Y]
    # print('列出原顺序    ',"p1:",sequence0,"p2:",sequence1)

    # 去掉已有基因
    for i in parent[0][X:Y]:  # 遍历中间交换部分
        if i in sequence0:  # 如果i在原序列中
            sequence0.remove(i)  # 就去掉这个值

    for i in parent[1][X:Y]:  # 遍历中间交换部分
        if i in sequence1:  # 如果i在原序列中
            sequence1.remove(i)  # 就去掉这个值
    print('去掉已有基因  ',"p1:",sequence0,"p2:",sequence1)

    # d. 从 第二个切点Y 后第一个位置起，将获得无重复顺序填入
    parent[0][Y:] = sequence0[:X]
    parent[0][:X] = sequence0[X:]

    parent[1][Y:] = sequence1[:X]
    parent[1][:X] = sequence1[X:]

    return parent

if __name__ == '__main__':
    print('交换完成         ',crossover())
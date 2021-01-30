# -*- coding: utf-8 -*-

# @File    : 纠删码画图.py
# @Date    : 2021-01-10
# @Author  : chenwei    -剑衣沉沉晚霞归，酒杖津津神仙来-
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')


def pltpicture(x, y,mode):
    plt.figure()
    plt.title("(k,3) RS %s time" % mode)
    plt.xlabel('k')
    plt.ylabel('%stime/s' % mode)

    plt.plot(x, y, '-o')
    plt.show()


# code time
# x = [42, 126, 200, 314 ,477]
# y = [1.293, 3.951, 6.337, 9.906,14.977]

# decode time
# x = [42, 126, 200, 314 ,477]
# y = [1.465, 4.227, 9.539, 14.798 ,24.321]

# 200k (6,m) code time
# x = [1, 2, 3, 4, 5]
# y = [5.897, 6.012, 6.215, 6.408, 6.6]

# decode time
# x = [1, 2, 3, 4, 5]
# y = [8.335, 8.651, 8.902, 9.172, 10.105]

# 200k (k,3) code time
x = [3, 4, 5, 6, 8, 10, 12, 14]
y = [6.349, 6.153, 6.015, (6.266+6.025)/2, 6.109, 6.068, 6.063, 6.13]

# 200k (k,3) decode time
xd = [3, 4, 5, 6, 8, 10, 12, 14]
yd = [9.575, 8.322, 8.196, (9.089+9.15)/2, 6.766, 7.73, 7.05, 6.82]
pltpicture(x, y, 'code')
pltpicture(xd, yd,'decode')

# -*- coding: utf-8 -*-

# @File    : 7-25 clockdeco_param.py模块：参数化clock装饰器.py
# @Date    : 2021-01-07
# @Author  : chenwei    -剑衣沉沉晚霞归，酒杖津津神仙来-
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ','.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))  # 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量
            # locals() 函数会以字典类型返回当前位置的全部局部变量
            return _result

        return clocked

    return decorate


# @clock 不会运行
@clock()
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(.2)

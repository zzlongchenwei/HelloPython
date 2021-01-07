# -*- coding: utf-8 -*-

# @File    : 6-9 MarcoCommand的各个实例都在内部存储着命令列表.py
# @Date    : 2021-01-02
# @Author  : 10717
# -剑衣沉沉晚霞归，酒杖津津神仙来-
class MacroCommand:
    """一个执行一组命令的命令"""
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()
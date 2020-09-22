#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/26

class Animal:
    def eat(self):
        print("----eat-----")


class Dog(Animal):
    pass

wangcai = Dog()
wangcai.eat
wangcai.eat()

# 继承，注意是个元组，别少了逗号
Cat = type("Cat", (Animal,),{})
xiaohuamao = Cat()
xiaohuamao.eat()


# __metaclass__属性

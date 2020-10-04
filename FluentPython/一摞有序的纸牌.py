"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/04  @author:zzlong  
@file:一摞有序的纸牌.py
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


# namedtuple() --> Returns a new subclass of tuple with named fields.


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):  # __getitem__方法让该类变成可迭代的
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # 方法index在列表中查找指定值第一次出现的索引
    return rank_value * len(suit_values) + suit_values[card.suit]
# rank_value即牌的值，len(suit_values)即乘4，因为有四个花色，2*4+(四个花色对应的值)不会与3*4+(四个花色对应的值)重复，
# suit_values[card.suit]花色的值


deck = FrenchDeck()
print(len(deck))

from random import choice

print(choice(deck))

# sorted函数会返回一个列表
for card in sorted(deck, key=spades_high):
    print(card)

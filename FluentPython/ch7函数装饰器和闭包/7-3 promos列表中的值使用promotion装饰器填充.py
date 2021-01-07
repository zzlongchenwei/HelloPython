# -*- coding: utf-8 -*-

# @File    : 7-3 promos列表中的值使用promotion装饰器填充.py
# @Date    : 2021-01-02
# @Author  : chenwei
# -剑衣沉沉晚霞归，酒杖津津神仙来-
promos = []


def promotion(promo_func):  # promotion把promo_func添加到promos列表中，然后原封不动地将其返回
    promos.append(promo_func)
    return promo_func


@promotion  # 被@promotion装饰的函数都会添加到promos列表中
def fidelity(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):  # best_promos无需修改，因为它依赖promos列表
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)

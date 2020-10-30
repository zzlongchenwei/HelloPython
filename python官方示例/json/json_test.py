#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:10717
@file:json_test.py
@time:2020/10/30
"""
import json

l1 = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(l1)

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))


from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())

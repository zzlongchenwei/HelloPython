"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/11  @author:zzlong  
@file:test.py
"""
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientCreator

class Greeter(Protocol):
  def sendMessage(self, msg):
    self.transport.write("MESSAGE %s/n" % msg)

def gotProtocol(p):
  p.sendMessage("Hello")
  reactor.callLater(1, p.sendMessage, "This is sent in a second")
  reactor.callLater(2, p.transport.loseConnection)

c = ClientCreator(reactor, Greeter)
c.connectTCP("localhost", 1234).addCallback(gotProtocol)


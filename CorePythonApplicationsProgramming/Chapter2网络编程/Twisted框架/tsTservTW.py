"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/11  @author:zzlong  
@file:tsTservTW.py
"""
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)

    def dataReceived(self, data):
        self.transport.write(bytes('[%s] %s' % (ctime(), data), 'utf-8'))
# 然后重写了 connectionMade()
# 和 dataReceived()方法，当一个客户端连接到服务器时就会执行 connectionMade()方法，
# 而当服务器接收到客户端通过网络发送的一些数据时就会调用 dataReceived()方法。
# reactor 会作为该方法的一个参数在数据中传输，这样就能在无须自己提取它的情况下访问


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection..')
reactor.listenTCP(PORT, factory)
reactor.run()
# 在服务器代码的最后部分中，创建了一个协议工厂。它之所以被称为工厂，是因为每次
# 得到一个接入连接时，都能“制造”协议的一个实例。然后在 reactor 中安装一个 TCP 监听
# 器，以此检查服务请求。当它接收到一个请求时，就会创建一个 TSServProtocol 实例来处理
# 那个客户端的事务。


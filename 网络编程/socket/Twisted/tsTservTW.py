#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/6/1
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print "...connection from:", clnt
    def dataReceived(self, data):
        self.transport.write('[%s] %s'%(ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print "waiting for connection..."
reactor.listenTCP(PORT, factory)
reactor.run()

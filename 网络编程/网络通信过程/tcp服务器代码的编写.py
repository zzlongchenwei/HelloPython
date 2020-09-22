#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -剑衣沉沉晚霞归，酒杖津津神仙来- #
# anuthor: zzlong time:2019/5/25

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", 4567))
serverSocket.listen(5)

clientSocket, clientInfo = serverSocket.accept()  # 返回值是一个元组
# clientSocket 表示这个新的客户端
# clientInfo 表示这个新的客户端的ip以及port

recvData = clientSocket.recv(1024)

print("%s:%s" % (str(clientInfo), recvData))

clientSocket.close()
serverSocket.close()

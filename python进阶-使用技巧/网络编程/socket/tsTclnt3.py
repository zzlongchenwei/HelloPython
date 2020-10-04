#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/14
from socket import *

HOST = '192.168.25.68' #or 'localhost'
PORT = 4567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()



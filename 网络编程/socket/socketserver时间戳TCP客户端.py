#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpClisock = socket(AF_INET, SOCK_STREAM)
    tcpClisock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpClisock.send(bytes('%s\r\n' % data,'utf-8'))
    data = tcpClisock.recv(BUFSIZ)
    if not data:
        break
    print(str(data.strip(),'utf-8'))
    tcpClisock.close()

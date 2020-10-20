"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/11  @author:zzlong  
@file:tsTclntSS.py
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


while True:
    # SocketServer 请求处理程序的默认行为是接受连接、获取请求，然后关闭连接。
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes(('%s\r\n' % data), 'utf-8'))
    # 因为这里使用的处理程序类对待套接字通信就像文件一样， 所以必须发送行终止符（回车和换行符）。
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8').strip())
    tcpCliSock.close()


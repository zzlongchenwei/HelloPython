"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/11  @author:zzlong  
@file:tsTservSS.py
"""

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)
# StreamRequestHandler类将输入和输出套接字看作类似文件的对象，


class MyRequestHandler(SRH):
    def handle(self):
        print('..connected from:', self.client_address)
        self.wfile.write(bytes('[%s] %s' % (ctime(), self.rfile.readline().decode('utf-8')), 'utf-8'))
        # self.wfile.write会有一个返回值，但是不知道是什么
        # write返回的是写入的字符长度。

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()

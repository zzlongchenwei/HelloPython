#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:filedownload_server.py
@time:2020/10/30
"""
import socket

def main():
    tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_sock.bind(("", 7890))

    tcp_server_sock.listen(128)

    new_clnt_sock, new_clnt_addr = tcp_server_sock.accept()

    file_name = new_clnt_sock.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载的文件是：%s" % (str(new_clnt_addr), file_name))

    new_clnt_sock.send(("hahhah------ok----").encode("utf-8"))

    new_clnt_sock.close()
    tcp_server_sock.close()

if __name__ == '__main__':
    main()

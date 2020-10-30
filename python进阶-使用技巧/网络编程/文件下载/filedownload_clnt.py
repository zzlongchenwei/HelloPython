#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:filedownload_clnt.py
@time:2020/10/30
"""

import socket

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    dest_ip = input('输入下载服务器的ip：')
    dest_port = input('输入下载服务器的port：')

    tcp_socket.connect((dest_ip, int(dest_port)))

    download_file_name = input('请输入要下载的文件名字：')

    tcp_socket.send(download_file_name.encode("utf-8"))

    recv_data = tcp_socket.recv(1024)

    with open("[new]" + download_file_name, "wb") as f:
        f.write(recv_data)

    tcp_socket.close()


if __name__ == '__main__':
    main()


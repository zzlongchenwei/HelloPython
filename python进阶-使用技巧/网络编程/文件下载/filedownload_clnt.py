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
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # dest_ip = input('输入下载服务器的ip：')
    # dest_port = input('输入下载服务器的port：')

    dest_ip = '192.168.129.129'
    dest_port = 7890
    # 2.链接客户端
    tcp_socket.connect((dest_ip, dest_port))
    # 3.输入要下载的文件名
    download_file_name = input('请输入要下载的文件名字：')
    # 4.发送要下载的文件名
    tcp_socket.send(download_file_name.encode("utf-8"))
    # 5.等待接收数据
    while True:
        recv_data = tcp_socket.recv(1024)
        # 6.保存数据
        if recv_data:
            with open("[new]" + download_file_name, "ab") as f:
                f.write(recv_data)
        else:
            break
    # 7.关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()


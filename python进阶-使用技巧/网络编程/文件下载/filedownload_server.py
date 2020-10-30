#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:zzlong
@file:filedownload_server.py
@time:2020/10/30
"""
import socket

def send_file_2_client(new_clnt_sock, new_clnt_addr):
    # 1.接收客户端发送来的需要下载的文件名
    file_name = new_clnt_sock.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载的文件是：%s" % (str(new_clnt_addr), file_name))
    file_content = None
    # 2.打开这个文件，读取数据
    try:
        f = open(file_name, "rb")
        while True:
            file_content = f.read(1024)
            if file_content:
                # 3.发送文件的数据给客户端
                new_clnt_sock.senda(file_content)
            else:
                break
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)



def main():
    # 1.创建套接字
    tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定本地信息
    tcp_server_sock.bind(("", 7890))
    # 3.监听
    tcp_server_sock.listen(128)
    while True:
        # 4.等待客户端的链接
        new_clnt_sock, new_clnt_addr = tcp_server_sock.accept()
        # 5.调用文件发送函数，完成为客户端服务
        send_file_2_client(new_clnt_sock, new_clnt_addr)
        # 6.关闭套接字
        new_clnt_sock.close()

    tcp_server_sock.close()

if __name__ == '__main__':
    main()

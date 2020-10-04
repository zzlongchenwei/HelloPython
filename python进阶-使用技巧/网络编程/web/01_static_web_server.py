#!/usr/bin/env python
# -*- coding: utf-8 -*-
# anuthor: zzlong time:2019/5/24

import socket
from multiprocessing import Process
HTML_ROOT_DIR = ""      # 命名规则 全为大写


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request data:",request_data)

    # 构造响应数据
    respose_start_line = "HTTP/1.1 200 OK\r\n"
    respose_headers = "Server: My_server\r\n"
    respose_body = "Helloooo"
    respose = respose_start_line + respose_headers + "\r\n" + respose_body
    print("respose data:", respose)

    # 向客户端返回数据
    client_socket.send(bytes(respose,"utf-8"))

    # 关闭客户端
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(("",8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        # print("[%s, %s]用户连接上了" % client_address[0], client_address[1])
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()




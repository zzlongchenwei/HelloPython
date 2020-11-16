#!/usr/bin/env python
# -*- coding: utf-8 -*-
# anuthor: zzlong time:2019/5/24
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# anuthor: zzlong time:2019/5/24

import socket
from multiprocessing import Process
import re

# 设置静态文件根目录
HTML_ROOT_DIR = "html"  # 设置常量命名规则 全为大写


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request data:",request_data)
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)

    # 解析请求报文
    # 'GET / HTTP/1.1'
    request_start_line = request_lines[0]
    # 提取用户请求的文件名
    file_name = re.match(tcp_server_socket"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"
    # 打开文件，读取内容
    try:
        file = open(HTML_ROOT_DIR + file_name,"rb")
    except IOError:
        respose_start_line = "HTTP/1.1 404 Not Found\r\n"
        respose_headers = "Server: My_server\r\n"
        respose_body = "The file is not found!"
    else:
        file_data = file.read()
        file.close()

        # 构造响应数据
        respose_start_line = "HTTP/1.1 200 OK\r\n"
        respose_headers = "Server: My_server\r\n"
        respose_body = file_data.decode("utf-8")

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




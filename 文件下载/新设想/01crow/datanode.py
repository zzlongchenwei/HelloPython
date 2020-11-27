#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:datanode.py
@time:2020/11/19
"""
import socket
import os
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import json


class datanode:
    def __init__(self, ADDR, user_id, BUFSIZE=1024):
        # 1.创建套接字
        self.clint_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 2.套接字地址
        self.clint_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 3.绑定地址
        self.clint_socket.bind(ADDR)

        self.BUFSIZE = BUFSIZE

        # 服务器信息
        self.namenode_addr = ('127.0.0.1', 7890)

        self.hello = ('%s:online' % user_id).encode('utf-8')
        self.bye = ('%s:offline' % user_id).encode('utf-8')

        # 上线
        self.my_online()

    def __del__(self):
        self.my_offline()
        self.clint_socket.close()

    def my_online(self):
        """上线"""
        self.clint_socket.sendto(self.hello, self.namenode_addr)
        # 接收信息，并解码
        recv_data, nn_addr = self.clint_socket.recvfrom(self.BUFSIZE)
        recv_data = self.recv_data_decode(recv_data)
        print(recv_data)

        if recv_data == 'hi':
            # 接收消息并解码
            recv_data, nn_addr = self.clint_socket.recvfrom(self.BUFSIZE)
            recv_data = self.recv_data_decode(recv_data)
            self.write_online_user_info(recv_data)


    def my_offline(self):
        """离线"""
        self.clint_socket.sendto(self.bye, self.namenode_addr)
        self.clint_socket.close()

    def recv_data_decode(self, recv_data):
        recv_data = recv_data.decode('utf-8')
        recv_data = json.loads(recv_data)
        return recv_data

    def write_online_user_info(self, online_user_info):
        """存储在线用户"""
        with open('online_user.json', 'w') as online:
            online.write(json.dumps(online_user_info))

    def read_online_user_info(self):
        with open('online_user.json', 'r') as online:
            online_user_info = json.loads(online.read())
        return online_user_info

    def get_file_size(self, filepath):
        """获取文件大小"""
        fsize = os.path.getsize(filepath)
        fsize = fsize / 1024  # kb单位

        return round(fsize, 2)

    def download_file(self):
        """数据接收"""
        # 输入要下载的文件名
        lookup = input('看看谁在线?(OK/NO)')
        if lookup == 'OK':
            online_user_info = self.read_online_user_info()
            print('在线的有:', online_user_info.keys())
        file_info = input('找谁下载，什么文件(user_id:file_name)')
        user_id, file_name = file_info.split(':')
        # 4.发送要下载的文件名
        self.clint_socket.sendto(file_name.encode("utf-8"), user_id)
        # 5.等待接收数据
        while True:
            recv_data, aim_addr = self.clint_socket.recvfrom(self.BUFSIZE)
            # 6.保存数据
            if recv_data:
                with open("./download/" + '[new]' + file_name, "ab") as f:
                    f.write(recv_data)
            else:
                break

    def send_file(self, file_name, aim_addr):
        """数据发送"""
        print("用户(%s)需要下载的文件是：%s" % (str(aim_addr), file_name))
        # 2.打开这个文件，读取数据
        try:
            with open('./download/' + file_name, "rb") as f:
                while True:
                    file_content = f.read(self.BUFSIZE)
                    if file_content:
                        # 3.发送文件的数据给客户端
                        self.clint_socket.sendto(file_content, aim_addr)
                    else:
                        break
        except Exception as e:
            print("没有要下载的文件(%s)" % file_name)

    def keep_communication(self):
        """持续接收namenode"""
        while True:
            # 接收消息并解码
            recv_data, nn_addr = self.clint_socket.recvfrom(self.BUFSIZE)
            recv_data = self.recv_data_decode(recv_data)
            self.write_online_user_info(recv_data)

    def keep_listen(self):
        """持续监听"""
        # 创建线程池
        listen_pool = ThreadPoolExecutor(max_workers=5)
        while True:
            # 1.接收客户端发送来的需要下载的文件名
            file_name, aim_addr = self.clint_socket.recv(self.BUFSIZE)
            file_name = file_name.decode('utf-8')
            listen_pool.submit(self.send_file, file_name, aim_addr)

    def keep_download(self):
        """持续下载"""
        # 创建线程池
        download_pool = ThreadPoolExecutor(max_workers=5)
        while True:
            down_flag = input("是否要下载？(Y/N) ")
            print('down_flag',down_flag)
            if down_flag == 'Y':
                print('down_flag',down_flag)
                download_pool.submit(self.download_file)

    def mult_thread(self):
        with ThreadPoolExecutor(max_workers=3) as thread_pool:
            thread_pool.submit(self.keep_communication)
            thread_pool.submit(self.keep_listen)
            thread_pool.submit(self.keep_download)


if __name__ == '__main__':
    ADDR = ('127.0.0.1', 7891)
    user_id = '1071707383'
    dn = datanode(ADDR, user_id)
    try:
        dn.mult_thread()
        while True:
            pass;
    finally:
        dn.__del__()
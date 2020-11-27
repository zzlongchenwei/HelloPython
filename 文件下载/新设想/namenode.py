#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
@author:chenwei
@file:namenode.py
@time:2020/11/19
"""
import socket
import json
from concurrent.futures import ThreadPoolExecutor
from pymysql import *


class namenode():
    def __init__(self, ADDR, BUFSIZE=1024):
        try:
            # 1.创建套接字
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # 2.套接字退出时，地址可以立即使用
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 3.绑定地址
            self.server_socket.bind(ADDR)

            self.BUFSIZE = BUFSIZE

            # 与数据库建立连接
            self.conn = connect(host='localhost', port=3306, user='root', password='weiwenhuamingZZ1',
                                database='crow_project', charset='utf8')  # 必须所有参数本地都有，不然不会成功

            # 初始化服务器用户状态
            self.init_database()

        except Exception:
            print("启动失败")

    """
    DATABASE操作
    """

    def __del__(self):
        """关闭游标，关闭连接"""
        print("close all")
        self.server_socket.close()
        self.init_database()
        self.conn.close()

    def init_database(self):
        """服务器启动时应该所有用户离线状态"""
        # 获得游标对象
        cursor = self.conn.cursor()
        sql = "UPDATE user_info SET status=2"
        cursor.execute(sql)
        cursor.close()
        self.conn.commit()

    def register(self, user_id):
        """用户注册"""
        cursor = self.conn.cursor()
        # id user_id ip port status
        try:
            sql = "INSERT INTO user_info VALUES (0,%s,default,default,default)"
            cursor.execute(sql, [user_id])
            cursor.close()
            self.conn.commit()
        except Exception:
            print("该 用户名/ID 已经被注册")

    def update_user_status(self, user_id, user_addr, status):
        """更新用户信息"""
        # 执行sql语句
        cursor = self.conn.cursor()
        ip, port = user_addr
        print("ip:", ip, "port:", port)
        sql = "UPDATE user_info SET ip=%s,port=%s,status=%s WHERE user_id=%s"
        cursor.execute(sql, [ip, port, status, user_id])
        cursor.close()
        self.conn.commit()
        print("更新用户信息完成")

    def count_online_user(self):
        """统计在线人数"""
        cursor = self.conn.cursor()
        sql = "SELECT count(*) FROM user_info WHERE status=1"
        cursor.execute(sql)
        online_num = cursor.fetchone()
        print("统计在线人数:", online_num[0])
        cursor.close()
        return online_num[0]

    def online_user_info(self):
        """其他在线用户信息"""
        cursor = self.conn.cursor()
        sql = "SELECT user_id,ip,port FROM user_info WHERE status=1"
        cursor.execute(sql)
        all_info = cursor.fetchall()
        send_info = dict()
        for one_user in all_info:
            # print("one_user:", one_user)
            user_id, ip, addr = one_user
            send_info[user_id] = (ip, addr)
        # print("send_info:", send_info)
        cursor.close()
        return send_info

    """
    SOCKET操作
    """

    def broadcast_update_info(self, send_info):
        """广播消息"""
        # print(online_user_info)
        send_info_json = json.dumps(send_info)
        for user_id, user_addr in send_info.items():
            # print(one_user)
            # print(tuple([ip, addr]))
            self.server_socket.sendto(send_info_json.encode('utf-8'), user_addr)
        print("广播完成")

    def connect_process(self, recv_data, client_addr):
        """连接时的处理"""
        print("1---","recv data:", recv_data, "client_addr", client_addr)
        # 数据格式为user_id:online
        user_id, status = recv_data.decode('utf-8').split(":")
        # print(user_id, type(user_id), status, type(user_id))
        print("2---","user_id:", user_id, "status:", status)

        if status == 'offline':
            # 更新数据库为离线状态
            self.update_user_status(user_id, client_addr, status)
            # 查询在线用户
            send_info = self.online_user_info()

            # 广播一次
            if self.count_online_user() > 0:
                self.broadcast_update_info(send_info)
            print("----%s已经离线----" % user_id)

        else:
            self.server_socket.sendto(json.dumps('hi').encode('utf-8'), client_addr)
            # 更新数据库为在线状态
            self.update_user_status(user_id, client_addr, status)
            # 查询在线用户
            send_info = self.online_user_info()
            print("3---",'查询在线用户', send_info)
            # 广播一次
            if self.count_online_user() > 0:
                self.broadcast_update_info(send_info)
                # 向该用户发送已在线用户信息
                # self.server_socket.sendto(str(online_user_info).encode('utf-8'), client_addr)
            print("----%s已上线----" % user_id)

    def thread_pool_process(self):
        """线程池处理"""
        # 创建线程池
        with ThreadPoolExecutor(max_workers=5) as process_pool:
            print('namenode已开启')
            while True:
                # 4.等待连接
                print("wait request")
                recv_data, client_addr = self.server_socket.recvfrom(self.BUFSIZE)
                process_pool.submit(self.connect_process, recv_data, client_addr)

if __name__ == '__main__':
    ADDR = ('', 7890)
    nn = namenode(ADDR)
    # nn.update_user_status(1071707383,('127.0.0.1',7891),1)
    try:
        nn.thread_pool_process()
    finally:
        nn.__del__()

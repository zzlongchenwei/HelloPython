"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/11  @author:zzlong  
@file:EchoProgramIPV6.py
"""

# Echo server program
import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    # AF_UNSPEC则意味着函数返回的是适用于指定主机名和服务名且适合任何协议族的地址。
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
        # 地址族、套接字类型和协议号
    except OSError as msg:
        # 此异常在一个系统函数返回系统相关的错误时将被引发，此类错误包括 I/O 操作失败例如 "文件未找到" 或 "磁盘已满" 等
        # （不包括非法参数类型或其他偶然性错误）。
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)

# socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
# 将 host/port 参数转换为 5 元组的序列，其中包含创建（连接到某服务的）套接字所需的所有参数。host 是域名，是字符串格式的 IPv4/v6 地址
# 或 None。port 是字符串格式的服务名称，如 'http' 、端口号（数字）或 None。传入 None 作为 host 和 port 的值，相当于将 NULL 传递给底层 C API。
#
# 可以指定 family、type 和 proto 参数，以缩小返回的地址列表。向这些参数分别传入 0 表示保留全部结果范围。flags 参数可以是 AI_* 常量中的一个或多个，
# 它会影响结果的计算和返回。例如，AI_NUMERICHOST 会禁用域名解析，此时如果 host 是域名，则会抛出错误。
#
# 本函数返回一个列表，其中的 5 元组具有以下结构：
#
# (family, type, proto, canonname, sockaddr)
#
# 在这些元组中，family, type, proto 都是整数且其作用是被传入 socket() 函数。 如果 AI_CANONNAME 是 flags 参数的一部分则 canonname 将是
# 表示 host 规范名称的字符串；否则 canonname 将为空。 sockaddr 是一个描述套接字地址的元组，其具体格式取决于返回的
# family (对于 AF_INET 为 (address, port) 2 元组，对于 AF_INET6 则为 (address, port, flowinfo, scope_id) 4 元组)，
# 其作用是被传入 socket.connect() 方法。
#
# 引发一个 审计事件 socket.getaddrinfo 附带参数 host、port、family、type、protocol。

# [(<AddressFamily.AF_INET6: 10>, <SocketType.SOCK_STREAM: 1>,
#  6, '', ('2606:2800:220:1:248:1893:25c8:1946', 80, 0, 0)),
#  (<AddressFamily.AF_INET: 2>, <SocketType.SOCK_STREAM: 1>,
#  6, '', ('93.184.216.34', 80))]
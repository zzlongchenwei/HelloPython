"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/11  @author:zzlong  
@file:采用原始套接字协议的 CAN 网络进行通信.py
"""
#  要改为通过广播管理器协议来使用 CAN，则要用以下方式打开一个 socket:
# socket.socket(socket.AF_CAN, socket.SOCK_DGRAM, socket.CAN_BCM)
# 在绑定 (CAN_RAW) 或连接 (CAN_BCM) socket 之后，你将可以在 socket 对象上正常使用 socket.send() 以及 socket.recv() 操作（及同类操作）。
import socket
import struct


# CAN frame packing/unpacking (see 'struct can_frame' in <linux/can.h>)

can_frame_fmt = "=IB3x8s"
can_frame_size = struct.calcsize(can_frame_fmt)

def build_can_frame(can_id, data):
    can_dlc = len(data)
    data = data.ljust(8, b'\x00')
    return struct.pack(can_frame_fmt, can_id, can_dlc, data)

def dissect_can_frame(frame):
    can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
    return (can_id, can_dlc, data[:can_dlc])


# create a raw socket and bind it to the 'vcan0' interface
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(('vcan0',))

while True:
    cf, addr = s.recvfrom(can_frame_size)

    print('Received: can_id=%x, can_dlc=%x, data=%s' % dissect_can_frame(cf))

    try:
        s.send(cf)
    except OSError:
        print('Error sending CAN frame')

    try:
        s.send(build_can_frame(0x01, b'\x01\x02\x03'))
    except OSError:
        print('Error sending CAN frame')

# 多次运行一个示例，且每次执行之间等待时间过短，可能导致这个错误:
# OSError: [Errno 98] Address already in use
# 这是因为前一次运行使套接字处于 TIME_WAIT 状态，无法立即重用。
# 要防止这种情况，需要设置一个 socket 标志 socket.SO_REUSEADDR:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind((HOST, PORT))
# SO_REUSEADDR 标志告诉内核将处于 TIME_WAIT 状态的本地套接字重新使用，而不必等到固有的超时到期。
#
# socket.setsockopt(level, optname, None, optlen: int)
# 设置给定套接字选项的值（参阅 Unix 手册页 setsockopt(2) ）。所需的符号常量（ SO_* 等）已定义在本 socket 模块中。
# 该值可以是整数、None 或表示缓冲区的 字节类对象。在后一种情况下，由调用者确保字节串中包含正确的数据位（关于将 C 结构体编码为字节串的方法，
# 请参阅可选的内置模块 struct ）。当 value 设置为 None 时，必须设置 optlen 参数。这相当于调用 setsockopt() C 函数时使用了 optval=NULL 和
# optlen=optlen 参数。
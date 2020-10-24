"""
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
-剑衣沉沉晚霞归，酒杖津津神仙来-
@time:2020/10/24  @author:zzlong  
@file:O上.py
"""

class IOTask:
    def terminate(self):
        self._runnig = False

    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)  # Set timeout period
        while self._runnig:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except sock.settimeout:
                continue
            # Continued processing
            # ...
        # Terminated
        return
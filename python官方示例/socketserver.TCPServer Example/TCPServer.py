"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/python
# -*- coding: UTF-8 -*-
@time:2020/10/11  @author:zzlong  
@file:socketserver.TCPServerExample.py
"""

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()


# An alternative request handler class that makes use of streams
# (file-like objects that simplify communication by providing the standard file interface):

# class MyTCPHandler(socketserver.StreamRequestHandler):
#
#     def handle(self):
#         # self.rfile is a file-like object created by the handler;
#         # we can now use e.g. readline() instead of raw recv() calls
#         self.data = self.rfile.readline().strip()
#         print("{} wrote:".format(self.client_address[0]))
#         print(self.data)
#         # Likewise, self.wfile is a file-like object used to write back
#         # to the client
#         self.wfile.write(self.data.upper())

# The difference is that the readline() call in the second handler will call recv() multiple times
# until it encounters a newline character, while the single recv() call
# in the first handler will just return what has been sent from the client in one sendall() call.


# $ python TCPServer.py
# 127.0.0.1 wrote:
# b'hello world with TCP'
# 127.0.0.1 wrote:
# b'python is nice'

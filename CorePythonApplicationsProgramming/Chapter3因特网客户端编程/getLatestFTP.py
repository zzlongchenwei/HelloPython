"""
-剑衣沉沉晚霞归，酒杖津津神仙来-
# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
@time:2020/10/14  @author:zzlong  
@file:getLatestFTP.py
"""

import ftplib
import os
import socket

HOST= 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror) as e:
        # socket.error
        # 一个被弃用的 OSError 的别名。
        # socket.gaierror
        # OSError 的子类，本异常来自 getaddrinfo() 和 getnameinfo()，表示与地址相关的错误。
        # 附带的值是一对 (error, string)，代表库调用返回的错误。string 表示 error 的描述，它由 C 函数 gai_strerror() 返回。
        # 数字值 error 与本模块中定义的 EAI_* 常量之一匹配。
        print('Error: cannot reach"%s"' % HOST)
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        # 当收到表示永久错误的错误代码（响应代码在500--599范围内）时引发异常。
        print('Error: cannot login anonymously')
        f.quit()
        return
    print('*** logged in an "anonymously"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('Error: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** Change to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
        # retrlines(cmd, callback=None)
        # 检索以编码参数在初始化时指定的编码方式列出的文件或目录。

        # retrbinary(cmd, callback, blocksize=8192, rest=None)
        # 检索二进制传输模式的文件。cmd应该是一个适当的RETR命令:'RETR filename'。对接收到的每个数据块调用回调函数，
        # 并使用单个字节参数给出数据块。可选的blocksize参数指定在创建来执行实际传输的低级套接字对象上读取的最大块大小
        # (它也将是传递给回调的数据块的最大大小)。选择一个合理的默认值。rest的意思与transfercmd()方法中的意思相同。

        # 如果提供了可选的rest，则将rest命令发送到服务器，并将rest作为参数传递。rest通常是请求文件中的一个字节偏移量，
        # 它告诉服务器在请求的偏移量处重新开始发送文件的字节，跳过初始字节。但是请注意，transfercmd()方法将rest转换为具有初始化时
        # 指定的编码参数的字符串，但是不检查字符串的内容。如果服务器不识别REST命令，将引发error_reply异常。如果发生这种情况，
        # 只需调用transfercmd()而不使用rest参数。
    except ftplib.error_perm:
        print('Error: cannot read file "%s"' % FILE)
        os.unlink(FILE)
        # 移除（删除）文件 path。该函数在语义上与 remove() 相同，unlink 是其传统的 Unix 名称。

    else:
        print('*** Downloaded "%s" to CWD' % FILE)
    f.quit()
    # 向服务器发送一个QUIT命令并关闭连接。这是关闭连接的“礼貌”方式，但如果服务器对QUIT命令响应错误，则可能引发异常。
    # 这意味着对close()方法的调用将使FTP实例对后续调用无效

    # FTP.close()
    # 单方面关闭连接。这不应该应用于已经关闭的连接，比如成功调用quit()之后。在此调用之后，
    # 不应该再使用FTP实例(在调用close()或quit()之后，您不能通过发出另一个login()方法来重新打开连接)。


if __name__ == '__main__':
    main()






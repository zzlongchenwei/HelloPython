#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/15

import os
from time import sleep
from tkinter import *

class Dirlist(object):

    def __init__(self, initdir=None):
        self.top = tk()
        self.label = Label(self.top, text='Directory Lister v0.1')
        self.label.pack()

        self.cwd = StringVar(self.top)

        self.dirl = Label(self.top, fg='blue', font=('Helvetica',12,'bold'))
        self.dirl.pack()


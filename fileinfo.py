# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:52:02 2019

@author: 18420
"""


import tkinter
from tkinter import Menu
from tkinter import scrolledtext
import tkinter.messagebox

import re
import os

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt

#读取文本文件
f = open('英语作文.txt')
ff = f.read()
l1 = []
line = ff.replace('.',' ').replace('!',' ').replace(',',' ').replace('?',' ').replace('  ',' ').replace(';',' ').replace("’",' ').replace("“",' ').replace("”",' ')
w = line.split()
for i in w:
    l1.append(i.lower())#去掉字符后小写化放入列表

#读取英文停用词表
f1 = open('英文停用词表.txt')
stopword = f1.readlines()
l2 = []
for i in stopword:
    i = i.strip()
    l2.append(i)#将停用词表放入列表

#去掉停用词后的单词放入列表
l3 = []
for i in l1:
    if i not in l2:
        l3.append(i)
    else:
        continue

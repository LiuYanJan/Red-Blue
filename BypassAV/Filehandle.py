# -*- coding:utf-8 -*-
'''
处理 CS 和 MSF 生成的 shellcode 文件
'''
import re


def handleCS(filename):
    df = open(filename, 'r', encoding='utf-8')
    for text in df.readlines():
        if r'\x' not in text:
            pass
        else:
            mess = re.search(r'"(\\.*)"', text).group(1)
    return mess


def handleMSF(filename):
    df = open(filename, 'r', encoding='utf-8')
    mes = ''
    for text in df.readlines():
        if r'\x' not in text:
            pass
        else:
            mess = re.search(r'"(\\.*)"', text).group(1)
            mes = mes + mess
    return mes


# 输入文件路径 提取 shellcode
#filename = 'E:\share\payload.c'
filename = 'E:\share\payload.py'
if r'.c' not in filename:
    mes = handleMSF(filename)
else:
    mes = handleCS(filename)

print(mes)


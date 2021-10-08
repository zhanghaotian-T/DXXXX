#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: 111.py
@time: 2021/10/06
"""


b = '1101'
i = 0
while b != '':
    i = i * 2 + (ord(b[0]) - ord('0'))
    b = b[1:]

print(i)

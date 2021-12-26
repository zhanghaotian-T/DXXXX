#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Connect_FTP.py
# @Time      :2021/12/22 23:13
# @Author    :Haotian
from Driver.xml_edit import BbuconfdbReconfig


class CetcbbuEdite(BbuconfdbReconfig):

    def __init__(self, file_path):
        BbuconfdbReconfig.__init__(self, file_path)



if __name__ == "__main__":
    run_code = 0

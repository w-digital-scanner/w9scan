#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__ = '1c3z'

import re

def assign(service, arg):
    if service == 'spider_file':
        return True, arg

def fetch(url,raw):
    card15 = r"\b([1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3})\b"
    card18 = r"\b([1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X))\b"
    URL = r"\b(http://(\d{1,3}\.){3}\d{1,3}(:\d+)?)\b"
    mail = r"\b([a-zA-Z\-_1-9]+@([a-zA-Z\-_1-9]+\.){1,3}(com|cn|net|org))\b"
    phone = r"\b((13|14|15|17|18)\d{9})\b"

    regexs = [card15,card18,mail,phone,URL]

    for r in regexs:
        rst = re.findall(r, raw)
        for i in rst:
            security_set("info",i[0],"Information Collect")

def audit(url,html):
    fetch(url,html)
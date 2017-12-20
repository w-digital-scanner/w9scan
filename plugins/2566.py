#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ =  Moxa NPort's web console! 未授权访问


def assign(service, arg):
    if service == "moxa_nport_router":
        return True, arg

def audit(arg):
    target =arg+"main.htm"
    code, head,res, errcode, _   = curl.curl2(target)
    if code == 200 and 'Change Password' in res and 'Accessible IP Settings' in res:
        security_hole(arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign("moxa_nport_router", 'http://175.138.62.157:8181/')[1])
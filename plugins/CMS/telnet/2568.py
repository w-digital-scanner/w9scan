#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ =  Moxa OnCell 未授权访问
#__appVersion__ = 'G3111,G3151'
import telnetlib

def assign(service, arg):
    if service == "telnet":
        return True, arg

def audit(arg):
    try:
        tn = telnetlib.Telnet(arg, port=23, timeout=10)
        key = tn.read_until('Console terminal type',timeout=10)
        tn.write('\n')
        tn.close()
        if key:
            security_hole('Moxa OnCell'+arg)
    except:
        pass
    
                                              
if __name__ == '__main__':
    from dummy import *
    audit(assign("telnet", '217.168.180.83')[1])
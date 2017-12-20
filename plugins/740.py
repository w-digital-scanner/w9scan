#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range
#refer:http://linux.im/2015/05/07/jQuery-1113-DomXSS-Vulnerability.html
#refer:http://www.beebeeto.com/pdb/poc-2015-0097/

import sys
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload = "wp-content/themes/twentyfifteen/genericons/example.html"
    verify_url = arg + payload
    code, head, res, _, _ = curl.curl(verify_url)
    if code == 200 and res.find('jquery/1.7.2/jquery.min.js"></script>') != -1:
        security_hole(verify_url + ': Wordpress /example.html jQuery DomXSS')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])

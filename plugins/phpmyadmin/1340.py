#!/usr/bin/env python
#-*- coding: utf-8 -*-
import re

def assign(service, arg):
    if service == "phpmyadmin":
        return True, arg

def audit(arg):
    t = ("themes/darkblue_orange/layout.inc.php",
    "libraries/lect_lang.lib.php",
    "libraries/mcrypt.lib.php",
    "libraries/export/xls.php",
    "libraries/select_lang.lib.php",
    "index.php?lang[]=1",
    "darkblue_orange/layout.inc.php",
    "phpinfo.php",
    "load_file()",
    "select_lang.lib.php")
    url = arg
    for s in t:
        
        code, head, res, errcode, _ = curl.curl(url + s)
        if code == 200:
            y = re.search('in <b>([^<]+)</b> on line <b>', res)
            if y:
                security_info(y.group(1))
            m = re.search('</a><h1 class="p">([^<]+)</h1>', res)
            if m:
                m2 = re.search('SCRIPT_FILENAME </td><td class="v">([^<]+)</td></tr>', res)
                security_info(m2.group(1))

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpmyadmin', 'http://www.wlsz.cn/')[1])
    audit(assign('phpmyadmin', 'http://www.miw.lpi.pl/phpmyadmin/')[1])
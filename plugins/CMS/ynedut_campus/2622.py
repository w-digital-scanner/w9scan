#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:YNedut Campus数字校园平台任意命令执行
#Refer:http://www.wooyun.org/bugs/wooyun-2014-050804
#Author:xq17

 
def assign(service, arg):
    if service == 'ynedut_campus':
    	return True,arg
def audit(arg):
    param_data = 'login/login!forwardFrameIndex.action'
    url = arg + param_data
    task_push('struts' ,url)
   
if __name__ == '__main__':
    from dummy import *
    audit(assign('ynedut_campus','http://117.141.5.246:8800/oa/')[1])
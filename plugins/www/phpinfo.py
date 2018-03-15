#!/usr/bin/env python
import re
import urlparse


def assign(service, arg):
    if service == "www":
        return True, arg


def audit(arg):
    phpinfoList = r"""
    phpinfo.php
PhpInfo.php
PHPinfo.php
PHPINFO.php
phpInfo.php
info.php
Info.php
INFO.php
test.php?mode=phpinfo
index.php?view=phpinfo
index.php?mode=phpinfo
TEST.php?mode=phpinfo
?mode=phpinfo
?view=phpinfo
install.php?mode=phpinfo
INSTALL.php?mode=phpinfo
admin.php?mode=phpinfo
phpversion.php
phpVersion.php
test1.php
test.php
test2.php
phpinfo1.php
phpInfo1.php
info1.php
PHPversion.php
x.php
xx.php
xxx.php
    """
    paths = phpinfoList.strip().splitlines()
    for path in paths:
        try:
            code, head, res, errcode, _ = curl.curl(arg + path)
        except:
            code = 0
            res = ""
        if code == 200 and "allow_url_fopen" in res:
            security_note("phpinfo leak:" + arg + path)


if __name__ == '__main__':
    from dummy import *

    audit(assign('www', 'http://127.0.0.1/')[1])

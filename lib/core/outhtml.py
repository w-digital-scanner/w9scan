#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.core.exception import BuildHtmlErrorException

class CollectData(object):
    def __init__(self):
        self.dict = dict()

    def add_list(self,k,v):
        if k == '':
            k = len(self.dict)
        if k not in self.dict:
            self.dict.setdefault(k,list())
        self.dict[k].append(v)
    
    def add_set(self,k,v):
        if k == '':
            k = len(self.dict)
        if k not in self.dict:
            self.dict.setdefault(k,set())
        self.dict[k].add(v)
            
    def getData(self):
        return self.dict

class buildHtml(object):

    def __init__(self):
        self.dict = dict()
        self.dict["info"] = CollectData()
        self.dict["note"] = CollectData()
        self.dict["warning"] = CollectData()
        self.dict["hole"] = CollectData()

    def add_list(self,level,value,k = ''):
        if level not in self.dict:
            raise BuildHtmlErrorException
        
        self.dict[level].add_list(k,value)

    def add_set(self,level,value,k = ''):
        if level not in self.dict:
            raise BuildHtmlErrorException
        self.dict[level].add_set(k,value)
    
    def build(self):
        htmlDict = dict()
        for key,value in self.dict.items():
            htmlDict[key] = value.getData()
        print str(htmlDict)

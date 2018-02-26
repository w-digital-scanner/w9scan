#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/boy-hack/w9scan
# author = w8ay
from lib.core.update import updateProgram
import sys,os
from lib.core.data import paths,logger,urlconfig
from lib.core.common import makeurl,printMessage
from lib.core.exception import ToolkitUserQuitException
from lib.core.exception import ToolkitMissingPrivileges
from lib.core.exception import ToolkitSystemException

def initOption(args):
    urlconfig.mutiurl = False
    urlconfig.url = []

    checkUpdate(args)
    searchPlguin(args)
    pluginScanRegister(args)

def checkUpdate(args):
    if args.update:
        updateProgram()
        sys.exit(0)

def searchPlguin(args):
    if args.search:
        name = args.search
        path = paths.w9scan_Plugin_Path
        plugins = os.listdir(path)
        foder = []
        for p in plugins:
            if name in p:
                foder.append(p)
        if not foder:
            logger.info("Not found the exp of '%s'"%(name))
        for f in foder:
            files = os.listdir(os.path.join(path,f))
            logger.info("Found:%-8s Total:%-4d Files:%-10s"%(f,len(files),str(files)))
        sys.exit(0)

def pluginScanRegister(args):
    if args.u and args.plugin:
        url = args.u
        if url.startswith("@"):
            urlconfig.mutiurl = True
            urlconfig.plugin = args.plugin
            fileName = url[1:]
            try:
                o = open(fileName,"r").readlines()
                for u in o:
                    urlconfig.url.append(makeurl(u.strip()))
            except IOError:
                raise ToolkitMissingPrivileges("Filename:'%s' open faild"%fileName)
            if len(o) == 0:
                raise ToolkitMissingPrivileges("The target address is empty")
            printMessage(urlconfig.url)
        else:
            urlconfig.url.append(makeurl(url))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/boy-hack/w9scan
# author = w8ay
from lib.core.update import updateProgram
import sys,os,logging,time
from lib.core.data import paths,logger,urlconfig
from lib.core.common import makeurl,printMessage
from lib.core.settings import LIST_PLUGINS
from lib.core.enums import CUSTOM_LOGGING
from lib.core.log import LOGGER
from lib.core.exception import ToolkitUserQuitException
from lib.core.exception import ToolkitMissingPrivileges
from lib.core.exception import ToolkitSystemException

def initOption(args):
    urlconfig.mutiurl = False
    urlconfig.url = []
    
    bannerOutput(args)
    setLoggingLevel(args)
    checkUpdate(args)  # 检测更新
    searchPlguin(args) # 查找插件
    pluginScanRegister(args) # 使用插件扫描
    guideRegister(args) # 向导模式

def setLoggingLevel(args):
    # Set FileHandler
    filename = os.path.join(paths.w9scan_Output_Path, "log" + "_" + str(int(time.time())) + ".txt")
    logger.info("The log file will be saved on: '%s'"%filename)
    FILE_HANDLER = logging.FileHandler(filename)   
    FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
    FILE_HANDLER.setFormatter(FORMATTER)
    LOGGER.addHandler(FILE_HANDLER)
    
    if args.debug:
        LOGGER.setLevel(CUSTOM_LOGGING.DEBUG)

def bannerOutput(args):
    if args.banner:
        sys.exit(0)
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
        urlconfig.mutiurl = True
        urlconfig.plugin = args.plugin
        
        if url.startswith("@"):
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

def guideRegister(args):
    inputUrl = raw_input('[1] Input url > ')
    if inputUrl is '':
        raise ToolkitSystemException("You have to enter the url")
    if inputUrl.startswith("@"):
        urlconfig.mutiurl = True
        fileName = inputUrl[1:]
        try:
            o = open(fileName,"r").readlines()
            for url in o:
                urlconfig.url.append(makeurl(url.strip()))
        except IOError:
            raise ToolkitSystemException("Filename:'%s' open faild"%fileName)
        if len(o) == 0:
            raise ToolkitSystemException("The target address is empty")
    else:
        urlconfig.url.append(makeurl(inputUrl))
    printMessage('[Prompt] URL has been loaded:%d' % len(urlconfig.url))
    printMessage("[Prompt] You can select these plugins (%s) or select all"%(' '.join(LIST_PLUGINS)))
    diyPlugin = raw_input("[2] Please select the required plugins > ")

    if diyPlugin.lower() == 'all':
        urlconfig.diyPlugin = LIST_PLUGINS
    else:
        urlconfig.diyPlugin = diyPlugin.strip().split(' ')

    printMessage("[Prompt] You select the plugins:%s"%(' '.join(urlconfig.diyPlugin)))
    urlconfig.scanport = False
    urlconfig.find_service = False
    if 'find_service' in urlconfig.diyPlugin:
        urlconfig.find_service = True
        input_scanport = raw_input('[2.1] Need you scan all ports ?(Y/N) (default N)> ')
        if input_scanport.lower() in ("y","yes"):
            urlconfig.scanport = True
    
    urlconfig.threadNum = raw_input('[3] You need start number of thread (default 5) > ')
    if urlconfig.threadNum == '':
        urlconfig.threadNum = 5

    urlconfig.threadNum = int(urlconfig.threadNum)
    urlconfig.deepMax = raw_input('[4] Set the depth of the crawler (default 100 | 0 don\'t use crawler ) > ')
    if urlconfig.deepMax == '':
        urlconfig.deepMax = 100
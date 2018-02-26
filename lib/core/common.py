#!/usr/bin/env python
#coding:utf-8
from lib.core.data import paths,logger
import sys
import os,re
from lib.core.settings import INVALID_UNICODE_CHAR_FORMAT
from lib.core.settings import banner
from thirdparty import hackhttp
from lib.core.log import LOGGER_HANDLER
import urlparse
import urllib2,urllib,time
from thirdparty.termcolor.termcolor import colored
from lib.core.convert import stdoutencode
from lib.core.enums import EXIT_STATUS

"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

def weAreFrozen():
    """
    Returns whether we are frozen via py2exe.
    This will affect how we find out where we are located.
    Reference: http://www.py2exe.org/index.cgi/WhereAmI
    """

    return hasattr(sys, "frozen")

def isListLike(value):
    """
    Returns True if the given value is a list-like instance

    >>> isListLike([1, 2, 3])
    True
    >>> isListLike(u'2')
    False
    """

    return isinstance(value, (list, tuple, set))

def getUnicode(value, encoding=None, noneToNull=False):
    """
    Return the unicode representation of the supplied value:

    >>> getUnicode(u'test')
    u'test'
    >>> getUnicode('test')
    u'test'
    >>> getUnicode(1)
    u'1'
    """

    if noneToNull and value is None:
        return "NULL"

    if isinstance(value, unicode):
        return value
    elif isinstance(value, basestring):
        while True:
            try:
                return unicode(value, encoding or "utf8")
            except UnicodeDecodeError, ex:
                try:
                    return unicode(value, "utf8")
                except:
                    value = value[:ex.start] + "".join(INVALID_UNICODE_CHAR_FORMAT % ord(_) for _ in value[ex.start:ex.end]) + value[ex.end:]
    elif isListLike(value):
        value = list(getUnicode(_, encoding, noneToNull) for _ in value)
        return value
    else:
        try:
            return unicode(value)
        except UnicodeDecodeError:
            return unicode(str(value), errors="ignore")  # encoding ignored for non-basestring instances

def setPaths(rootPath):
    """
    Sets absolute paths for project directories and files
    """

    paths.w9scan_ROOT_PATH = rootPath

    # w9scan paths
    paths.w9scan_Plugin_Path = os.path.join(paths.w9scan_ROOT_PATH, "plugins")
    paths.w9scan_Output_Path = os.path.join(paths.w9scan_ROOT_PATH, "output")

def Banner():
    """
    Function prints banner with its version
    """
    _ = banner
    if not getattr(LOGGER_HANDLER, "is_tty", False):
        _ = re.sub("\033.+?m", "", _)
    dataToStdout(_)

def makeurl(url):
    prox = "http://"
    if (url.startswith("https://")):
        prox = "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        url = prox + url
    url_info = urlparse.urlparse(url)
    
    if url_info.path:
        url = prox + url_info.netloc + url_info.path
        if not url.endswith("/"):
            url = url + "/"
    else:
        url = prox + url_info.netloc + "/"
    return url

def createIssueForBlog(errMSG):
    """
    Automatically create a blog comment with unhandled exception information
    """
    hh = hackhttp.hackhttp()
    postData = "gid=213&pid=0&qqnum=&comname=w9scan+BugReporter&commail=buger%40hacking8.com&comurl=&private=on&comment=%5B%E7%A7%81%E5%AF%86%E8%AF%84%E8%AE%BA%5D%E6%8A%A5%E5%91%8Abug:" + errMSG
    code, head, body, redirect, log = hh.http('https://blog.hacking8.com/index.php?action=addcom', post=postData)

def runningTime(time):
    sTime = round(time,2)
    mTime = round(time/60,2)
    timeStr = "%s min / %s seconds"%(str(mTime),str(sTime))
    return timeStr

def dataToStdout(data, forceOutput=False, bold=False, content_type=None):
    """
    Writes text to the stdout (console) stream
    """
    if isinstance(data, unicode):
        message = stdoutencode(data)
    else:
        message = data
    sys.stdout.write(setColor(message, bold))
    try:
        sys.stdout.flush()
    except IOError:
        pass

def setColor(message, bold=False):
    retVal = message

    if message and getattr(LOGGER_HANDLER, "is_tty", False):  # colorizing handler
        if bold:
            retVal = colored(message, color=None, on_color=None, attrs=("bold",))

    return retVal
def pollProcess(process, suppress_errors=False):
    """
    Checks for process status (prints . if still running)
    """

    while True:
        dataToStdout(".")
        time.sleep(1)

        returncode = process.poll()

        if returncode is not None:
            if not suppress_errors:
                if returncode == 0:
                    dataToStdout(" done\n")
                elif returncode < 0:
                    dataToStdout(" process terminated by signal %d\n" % returncode)
                elif returncode > 0:
                    dataToStdout(" quit unexpectedly with return code %d\n" % returncode)

            break

def getSafeExString(ex, encoding=None):
    """
    Safe way how to get the proper exception represtation as a string
    (Note: errors to be avoided: 1) "%s" % Exception(u'\u0161') and 2) "%s" % str(Exception(u'\u0161'))

    >>> getSafeExString(Exception('foobar'))
    u'foobar'
    """

    retVal = ex

    if getattr(ex, "message", None):
        retVal = ex.message
    elif getattr(ex, "msg", None):
        retVal = ex.msg

    return getUnicode(retVal or "", encoding=encoding).strip()

def systemQuit(status=EXIT_STATUS.SYSETM_EXIT):
    if status == EXIT_STATUS.SYSETM_EXIT:
        logger.info('System exit.')
    elif status == EXIT_STATUS.USER_QUIT:
        logger.error('User quit!')
    elif status == EXIT_STATUS.ERROR_EXIT:
        logger.error('System exit.')
    sys.exit(0)

def printMessage(msg):
    dataToStdout('\r' + msg + '\n\r')
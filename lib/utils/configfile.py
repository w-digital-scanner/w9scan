#!/usr/bin/env python

"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""
import os
import codecs
from lib.core.data import logger
from ConfigParser import RawConfigParser,DEFAULTSECT
from lib.core.exception import ToolkitSystemException
from lib.core.common import getUnicode,unArrayizeValue
from lib.core.enums import OPTION_TYPE
from lib.core.data import w9config

config = None

optDict = {
    "Config":{
        "thread":            "integer",
        "crawlerDeep":               "integer",
        "TimeOut":           "integer",
        "UserAgent":          "string",
        "Cookie":       "string",
        "headers":       "string"
    }
}                             

def configFileProxy(section, option, datatype):
    """
    Parse configuration file and save settings into the configuration
    advanced dictionary.
    """

    global config

    if config.has_option(section, option):
        try:
            if datatype == OPTION_TYPE.BOOLEAN:
                value = config.getboolean(section, option) if config.get(section, option) else False
            elif datatype == OPTION_TYPE.INTEGER:
                value = config.getint(section, option) if config.get(section, option) else 0
            elif datatype == OPTION_TYPE.FLOAT:
                value = config.getfloat(section, option) if config.get(section, option) else 0.0
            else:
                value = config.get(section, option)
        except ValueError, ex:
            errMsg = "error occurred while processing the option "
            errMsg += "'%s' in provided configuration file ('%s')" % (option, getUnicode(ex))
            raise ToolkitSystemException(errMsg)

        if value:
            w9config[option] = value
        else:
            w9config[option] = None
    else:
        debugMsg = "missing requested option '%s' (section " % option
        debugMsg += "'%s') into the configuration file, " % section
        debugMsg += "ignoring. Skipping to next."
        logger.debug(debugMsg)

def openFile(filename, mode='r', encoding="utf8", errors="replace", buffering=1):  # "buffering=1" means line buffered (Reference: http://stackoverflow.com/a/3168436)
    """
    Returns file handle of a given filename
    """

    try:
        return codecs.open(filename, mode, encoding, errors, buffering)
    except IOError:
        errMsg = "there has been a file opening error for filename '%s'. " % filename
        errMsg += "Please check %s permissions on a file " % ("write" if \
          mode and ('w' in mode or 'a' in mode or '+' in mode) else "read")
        errMsg += "and that it's not locked by another process."
        raise ToolkitSystemException(errMsg)

def checkFile(filename, raiseOnError=True):
    """
    Checks for file existence and readability
    """

    valid = True

    try:
        if filename is None or not os.path.isfile(filename):
            valid = False
    except UnicodeError:
        valid = False

    if valid:
        try:
            with open(filename, "rb"):
                pass
        except:
            valid = False

    if not valid and raiseOnError:
        raise ToolkitSystemException("unable to read file '%s'" % filename)

    return valid

class UnicodeRawConfigParser(RawConfigParser):
    """
    RawConfigParser with unicode writing support
    """

    def write(self, fp):
        """
        Write an .ini-format representation of the configuration state.
        """

        if self._defaults:
            fp.write("[%s]\n" % DEFAULTSECT)

            for (key, value) in self._defaults.items():
                fp.write("%s = %s\n" % (key, getUnicode(value, "UTF8").replace('\n', '\n\t')))

            fp.write("\n")

        for section in self._sections:
            fp.write("[%s]\n" % section)

            for (key, value) in self._sections[section].items():
                if key != "__name__":
                    if value is None:
                        fp.write("%s\n" % (key))
                    else:
                        fp.write("%s = %s\n" % (key, getUnicode(value, "UTF8").replace('\n', '\n\t')))

            fp.write("\n")

def configFileParser(configFile):
    """
    Parse configuration file and save settings into the configuration
    advanced dictionary.
    """

    global config

    debugMsg = "parsing configuration file"
    logger.debug(debugMsg)

    checkFile(configFile)
    configFP = openFile(configFile, "rb")

    try:
        config = UnicodeRawConfigParser()
        config.readfp(configFP)
    except Exception, ex:
        errMsg = "you have provided an invalid and/or unreadable configuration file ('%s')" % ex
        raise ToolkitSystemException(errMsg)

    if not config.has_section("Config"):
        errMsg = "missing a mandatory section 'Config' in the configuration file"
        raise ToolkitSystemException(errMsg)

    mandatory = False

    for option in ("thread","crawlerDeep","TimeOut","UserAgent","Cookie","headers"):
        if config.has_option("Config", option):
            mandatory = True
            break

    if not mandatory:
        errMsg = "missing a mandatory option in the configuration file "
        errMsg += "(direct, url, logFile, bulkFile, googleDork, requestFile, sitemapUrl or wizard)"
        raise ToolkitSystemException(errMsg)

    for family, optionData in optDict.items():
        for option, datatype in optionData.items():
            datatype = unArrayizeValue(datatype)
            configFileProxy(family, option, datatype)
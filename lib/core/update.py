#!/usr/bin/env python
import os
from lib.core.data import paths,logger
from lib.core.common import dataToStdout,pollProcess,getSafeExString
from lib.core.settings import GIT_REPOSITORY
import time
import subprocess,locale
from lib.core.revison import getRevisionNumber
import re

def updateProgram():
    success = False

    if not os.path.exists(os.path.join(paths.w9scan_ROOT_PATH, ".git")):
        errMsg = "not a git repository. Please checkout the 'boy-hack/w9scan' repository "
        errMsg += "from GitHub (e.g. 'git clone --depth 1 https://github.com/boy-hack/w9scan.git w9scan')"
        logger.critical(errMsg)
    else:
        infoMsg = "updating w9scan to the latest development version from the "
        infoMsg += "GitHub repository"
        logger.info("\r[%s] [INFO] %s"%(time.strftime("%X"),infoMsg))

        debugMsg = "w9scan will try to update itself using 'git' command"
        logger.info(debugMsg)

        dataToStdout("\r[%s] [INFO] update in progress " % time.strftime("%X"))
    
    try:
        process = subprocess.Popen("git checkout . && git pull %s HEAD" % GIT_REPOSITORY, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=paths.w9scan_ROOT_PATH.encode(locale.getpreferredencoding()))  # Reference: http://blog.stastnarodina.com/honza-en/spot/python-unicodeencodeerror/
        pollProcess(process, True)
        stdout, stderr = process.communicate()
        success = not process.returncode
    except (IOError, OSError), ex:
        success = False
        stderr = getSafeExString(ex)

    if success:
        logger.info("\r[%s] [INFO] %s the latest revision '%s'" % (time.strftime("%X"),"already at" if "Already" in stdout else "updated to", getRevisionNumber()))
    else:
        if "Not a git repository" in stderr:
            errMsg = "not a valid git repository. Please checkout the 'boy-hack/w9scan' repository "
            errMsg += "from GitHub (e.g. 'git clone --depth 1 https://github.com/boy-hack/w9scan.git sqlmap')"
            logger.critical(errMsg)
        else:
            logger.critical("update could not be completed ('%s')" % re.sub(r"\W+", " ", stderr).strip())

    if not success:
        if subprocess.mswindows:
            infoMsg = "for Windows platform it's recommended "
            infoMsg += "to use a GitHub for Windows client for updating "
            infoMsg += "purposes (http://windows.github.com/) or just "
            infoMsg += "download the latest snapshot from "
            infoMsg += "https://github.com/boy-hack/w9scan"
        else:
            infoMsg = "for Linux platform it's required "
            infoMsg += "to install a standard 'git' package (e.g.: 'sudo apt-get install git')"

        print("\r[%s] [INFO] %s"%(time.strftime("%X"),infoMsg))

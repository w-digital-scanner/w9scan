#!/usr/bin/env python

# w9scan version
VERSION = "1.8.3"
Site = "https://github.com/boy-hack/w9scan"
AUTHOR = "w8ay"
MAIL = "master@hacking8.com"

# w9scan banner
banner = """\033[01;34m
           ____                       \033[01;31m__/\033[01;34m
 _      __/ __ \______________ _____ \033[01;33m/ \033[01;31m__/\033[01;34m
| | /| / / /_/ / ___/ ___/ __ `/ __ \\ \033[01;33m_/\033[01;34m
| |/ |/ /\__, (__  ) /__/ /_/ / / / /
|__/|__//____/____/\___/\__,_/_/ /_/

\033[01;37m{\033[01;m Version %s by %s mail:%s \033[01;37m}\033[0m
\n""" % (VERSION, AUTHOR, MAIL)


# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\x%02x"

# Selectable list of plugins
LIST_PLUGINS = ["subdomain","find_service","whatcms","struts","fuzz"]

GIT_REPOSITORY = "https://github.com/boy-hack/w9scan.git"
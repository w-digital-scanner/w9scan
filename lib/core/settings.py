#!/usr/bin/env python

import subprocess

# w9scan version
VERSION = "1.8.5"
Site = "https://github.com/boy-hack/w9scan"
AUTHOR = "w8ay"
MAIL = "master@hacking8.com"

IS_WIN = subprocess.mswindows

# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\x%02x"
# Encoding used for Unicode data
UNICODE_ENCODING = "utf-8"

# Selectable list of plugins
LIST_PLUGINS = ["subdomain","find_service","whatcms","struts","fuzz"]

GIT_REPOSITORY = "https://github.com/boy-hack/w9scan.git"

# Select random banner

banner_0 = """\033[01;34m
            ____                        \033[01;31m__/\033[01;34m
 _      __ / __ \  ____________________\033[01;33m/\033[01;31m__/\033[01;34m
| | /| / // /_/ / / ___/ ___/ __ `/ __ \\\033[01;33m_/\033[01;34m
| |/ |/ / \__, / (__  ) /__/ /_/ / / / /
|__/|__/ /____/ /____/\___/\__,_/_/ /_/

\033[01;37m{ \033[01;m Version %s by %s   \033[01;37m}\033[0m
\n""" % (VERSION, AUTHOR)

banner_1 = """\033[01;34m
 _____________________________
< w9scan Version:%s by %s >
 -----------------------------\033[0m
     \033[01;31m\\
      \033[01;33m\\\033[0m
          oO)-.                       .-(Oo
         /__  _\                     /_  __\\
         \  \(  |     ()~()         |  )/  /
          \__|\ |    (-___-)        | /|__/
          '  '--'    ==`-'==        '--'  '

""" % (VERSION, AUTHOR)

banner_2 = """\033[01;34m
 _____________________________
< w9scan Version:%s by %s >
 -----------------------------\033[0m
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||

""" % (VERSION, AUTHOR)

banner_3 = """\033[01;34m
_____________________________
< w9scan Version:%s by %s >
-----------------------------\033[0m
  \033[01;31m\\
    \033[01;33m\\\033[0m
      .--.
     |o_o |
     |:_/ |
    //   \ \\
   (|     | )
   /'\_   _/`\\
   \___)=(___/

"""% (VERSION, AUTHOR)

banners = [banner_0,banner_1,banner_2,banner_3]
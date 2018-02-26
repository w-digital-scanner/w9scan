#!/usr/bin/env python

"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.datatype import AttribDict
from lib.core.log import MY_LOGGER

logger = MY_LOGGER

# w9scan paths
paths = AttribDict()

# w9scan cmder
cmdLineOptions = AttribDict()

# w9scan urlconfig
urlconfig = AttribDict()

# w9scan plugins pycode hash
w9_hash_pycode = dict()
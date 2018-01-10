#!/usr/bin/env python

# w9scan version
VERSION = "1.6.0"
Site = "https://blog.hacking8.com/"

# w9scan banner
banner = """
        (()___(()
        /        \\
       ( /     \  \       W9scan v%s is running!
        \ o  o    /    
        (_()__)__/ \      Author:w8ay      
       / __,==.____ \   
      (    |--|      )    Email: w8ay@qq.com
      /\_..|__|'-.__/\_
     / (         /     \  Blog: %s
     \  \       (      /
      )  '.______)    /  
   (((____.---(((____/
"""%(VERSION,Site)


# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\x%02x"
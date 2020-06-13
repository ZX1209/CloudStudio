## unar


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import zipfile

file = zipfile.ZipFile(sys.argv[1], "r")
for name in file.namelist():
    utf8name = name.decode('gbk')

    pathname = os.path.dirname(utf8name)
    if not os.path.exists(pathname) and pathname != "":
        os.makedirs(pathname)
    data = file.read(name)
    if not os.path.exists(utf8name):
        fo = open(utf8name, "w")
        fo.write(data)
        fo.close
file.close()
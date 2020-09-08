#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import os
import subprocess
import datetime

file_path = Path(__file__).absolute()
file_dir_path = file_path.parent
original_working_path = Path("./").absolute()


# todo: vscdoe extension list and auto install

# todo: vscode user settings...
# note: also a version in github...

vs_code_extensions_list_file = Path("")

result = subprocess.run(["code", "--list-extensions"], capture_output=True)
extensions_str = str(result.stdout, "utf-8")
extension_list = extensions_str.split("\n")


# back to pre dir
os.chdir(pre_dir)

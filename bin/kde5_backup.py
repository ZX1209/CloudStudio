#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import os
import subprocess
import datetime

file_path = Path(__file__).absolute()
file_dir_path = file_path.parent
original_working_path = Path("./").absolute()


# todo: need backup list
need_backup_files = []
file_dir = Path("/home/gl/.config")

# glob files
need_backup_files.extend(file_dir.glob("k*"))
need_backup_files.extend(file_dir.glob("plasma*"))

# push working dir
archive_dir = Path("/home/gl/Archive/Category-backup")
pre_dir = Path.cwd()
os.chdir(archive_dir)

archive_file_name = datetime.datetime.now().isoformat()[:19] + "--kde5_backup.zip"

# todo: first calculate the size,use du

# calc_size_cmd = [
#     "du",
#     "-sh",
#     *need_backup_files,  # unpack list to list
# ]
# subprocess.run(calc_size_cmd)


# todo: stop?

backup_cmd = [
    "zip",
    archive_file_name,
    *need_backup_files,  # unpack list to list
]

subprocess.run(backup_cmd)


# back to pre dir
os.chdir(pre_dir)

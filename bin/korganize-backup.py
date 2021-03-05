#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import os
import subprocess
import datetime

file_path = Path(__file__).absolute()
file_dir_path = file_path.parent
original_working_path = Path("./").absolute()

# const
file_dir = Path("/home/gl/Projects/calendars-日历/")
archive_dir = Path(
    "/home/gl/gl_home/archive/category-backup/calendars"
)  # todo: should touch if this exists


# done: need backup list
need_backup_files = []

# glob files
need_backup_files.extend(file_dir.glob("*.ics"))

# push working dir
pre_dir = Path.cwd()
os.chdir(archive_dir)

#
archive_file_name = datetime.datetime.now().isoformat()[:13] + "--calendars-backup.zip"

# todo: first calculate the size,use du

# calc_size_cmd = [
#     "du",
#     "-sh",
#     *need_backup_files,  # unpack list to list
# ]
# subprocess.run(calc_size_cmd)


backup_cmd = [
    "zip",
    archive_file_name,
    *need_backup_files,  # unpack list to list
]

subprocess.run(backup_cmd)


# back to pre dir
os.chdir(pre_dir)

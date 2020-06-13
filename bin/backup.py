#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import os
import

# todo: first calculate the size,use du


# todo: storefile list
backup_file_cards = [
    "/etc",
    "/home/gl/.config",
    # kde settings
    "/home/gl/.config/k*",
    "/home/gl/.config/plasma*",
    # cloudstudio
    "/home/gl/CloudStudio",
    "/home/gl/.bashrc"
]
# todo: exclude list?
archive_dir = Path("/home/gl/Archive/Category-backup")

file_path = Path(__file__).absolute()
file_dir_path = file_path.parent
original_working_path = Path("./").absolate()
os.chdir(file_dir_path)

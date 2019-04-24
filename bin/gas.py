#!/usr/bin/env python3

# git auto save

from clara import ThirdShell
from pathlib import Path
import os


if ThirdShell.NoInternetConnected():
    print("no internet connected")
else:
    home = Path.home()
    os.chdir(home/'CloudStudio')

    ThirdShell.runCmdStrs(
        [
            'git pull ',
            'git add --all',
            'git commit -m "auto commit     by git-auto-save.py" ',
            'git push'
        ]
    )

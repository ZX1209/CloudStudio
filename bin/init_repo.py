#!/usr/bin/python3
import argparse

# import sys
from clara import ThirdShell
import requests
from pathlib import Path
import logging as log

log.basicConfig(level=log.INFO)
log.debug("this is a demo massage")

cwd = Path.cwd()
# #
# cmd_atgs_list = " add ".split()

# setup
parser = argparse.ArgumentParser()
parser.add_argument("userName")
parser.add_argument("userPass")
# type choices action default...


def init_repo(args=None):
    """main
    init_repo {{userName}} {{ userPass }}
    """
    # args parser
    # default is sys.argv
    # can be a [str]
    args = parser.parse_args(args)

    # init commit
    ThirdShell.runCmdStrs(
        [
            "git init",
            "git add --all",
            "git commit -m 'auto commmit for init a github repo'",
        ]
    )

    # create a repo
    log.info("start request")
    response = requests.post(
        "https://api.github.com/user/repos",
        json={"name": cwd.name},
        auth=(args.userName, args.userPass),
    )

    if response:
        ThirdShell.runCmdStrs(
            [
                f"git remote add origin https://github.com/ZX1209/{cwd.name}.git",
                "git push --set-upstream origin master",
            ]
        )
        log.info("success")
    else:
        log.error(response.json())


if __name__ == "__main__":
    init_repo()
